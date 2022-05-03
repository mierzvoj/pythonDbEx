import bcrypt as bcrypt

from database.database import Database
from .user_model import User

LOGIN_RE = r'^[a-zA-Z0-9]+$'
db = Database()


# def create_user(login, password):
#     salt = bcrypt.gensalt()
#     password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
#     D = {'key1': login, 'key2':password}
#     db.insertIntoUsers(D)


def create_user(login, password):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    # print("logina:", login, "passworda:", password)
    # print(type(login.lower()))
    # print(type(password))
    db.insertIntoUsers(login.lower(), password)
    # db.insertIntoUsers(login.lower(), password, "cycki")
