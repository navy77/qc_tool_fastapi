from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os
from dotenv import load_dotenv
import urllib.parse
import pymssql

load_dotenv()

server = os.getenv("SERVER")
database = os.getenv("DATABASE")
user_login = os.getenv("USER_LOGIN")
password = os.getenv("PASSWORD")

encoded_password = urllib.parse.quote_plus(password)

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db_connection():
    return pymssql.connect(server=server, user=user_login, password=password, database=database)

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


@router.post("/", response_model=schemas.Measure)
def create_measure(measure: schemas.MeasureCreate, db: Session = Depends(database.get_db)):
    return crud.create_measure(db=db, measure=measure)

@router.post("/register/",response_model=schemas.User)
def register(user: schemas.UserCreate):

    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = get_password_hash(user.password)
    cursor.execute("INSERT INTO users (email, hashed_password, role) VALUES (%s, %s, %d)", (user.email, hashed_password, user.role))
    conn.commit()
    conn.close()
    return {"email": user.email}

def create_calibration(db: Session, calibration: schemas.CalibrationCreate):
    db_calibration = models.Calibration(**calibration.dict())
    db.add(db_calibration)
    db.commit()
    db.refresh(db_calibration)
    return db_calibration