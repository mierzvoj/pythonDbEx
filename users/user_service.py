import bcrypt as bcrypt

from database.database import Database
from .user_model import User

LOGIN_RE = r'^[a-zA-Z0-9]+$'

db = Database

def create_user(login: str, password):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    db.insertIntoUsers(login.lower(), password)
