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
        else:
            print("wrong number")
    return


def register_user():
    login = input("Login:")
    password = getpass.getpass("Password:")
    user_service.create_user(login, password)


if __name__ == '__main__':
    run()
