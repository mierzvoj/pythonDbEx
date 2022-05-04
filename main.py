import sys
import getpass

from database.database import Database
from users import user_service


def run():
    db = Database()
    db.createTableRooms()
    db.createTableUsers()

    if sys.argv[1] == "user":
        if sys.argv[2] == "register":
            register_user()
        if sys.argv[2] == "login":
            login(db)
        else:
            print("wrong number")
    return

def register_user():
    login = input("Login:")
    password = getpass.getpass("Password:")
    user_service.create_user(login, password)

def login(db):
    login = input("Login:")
    password = getpass.getpass("Password:")
    return user_service.login(db, login, password)


if __name__ == '__main__':
    run()
