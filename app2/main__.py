from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
import pymssql

# FastAPI setup
app = FastAPI()

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database connection setup
DB_SERVER = "192.168.1.30"
DB_USER = "sa"
DB_PASSWORD = "sa$admin"
DB_NAME = "qc_db"

def get_db_connection():
    return pymssql.connect(server=DB_SERVER, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

# Models
class UserCreate(BaseModel):
    email: str
    password: str
    role: int = 2  # Default role is user

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(conn, email: str):
    cursor = conn.cursor(as_dict=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    return cursor.fetchone()

def authenticate_user(conn, email: str, password: str):
    user = get_user_by_email(conn, email)
    if not user or not verify_password(password, user['hashed_password']):
        return False
    return user

def get_current_user(token: str = Depends(oauth2_scheme)):
    conn = get_db_connection()
    user = get_user_by_email(conn, token)
    conn.close()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def get_current_active_user(current_user = Depends(get_current_user)):
    if current_user['role'] not in [1, 2]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_admin_user(current_user = Depends(get_current_active_user)):
    if current_user['role'] != 1:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return current_user

@app.post("/register/")
def register(user: UserCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = get_password_hash(user.password)
    cursor.execute("INSERT INTO users (email, hashed_password, role) VALUES (%s, %s, %d)", (user.email, hashed_password, user.role))
    conn.commit()
    conn.close()
    return {"email": user.email}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = get_db_connection()
    user = authenticate_user(conn, form_data.username, form_data.password)
    conn.close()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user['email'], "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(current_user = Depends(get_current_active_user)):
    return current_user

@app.get("/admin")
def read_admin_data(current_user = Depends(get_current_admin_user)):
    return {"message": "This is an admin-only endpoint."}
