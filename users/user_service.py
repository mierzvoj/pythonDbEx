from getpass import getpass

import bcrypt as bcrypt

from database.database import Database
from .user_model import User

LOGIN_RE = r'^[a-zA-Z0-9]+$'
db = Database()


def create_user(login, password):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    db.insertIntoUsers(login.lower(), password)


def login(db: Database, login, password):
    user = db.find_in_db(login.lower(), password)
    print(user)
    if user is None:
        return None
    if not bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
        return None
    print(user[1])
    return User(login=user[1])


