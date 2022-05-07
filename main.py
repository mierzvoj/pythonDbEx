import sys
import getpass

import click

import rooms
from database.database import Database
from rooms import room_service
from users import user_service


@click.group()
def run():
    db = Database()
    db.createTableRooms()
    db.createTableUsers()

    # if sys.argv[1] == "user":
    #     if sys.argv[2] == "register":
    #         register_user()
    #     if sys.argv[2] == "login":
    #         user = login(db)
    #         if user is None:
    #             print("Wrong credentials!")
    #             return
    #     if sys.argv[3] == "list":
    #         list_all_users(db)
    #     if sys.argv[3] == "findone":
    #         find_user_by_login(db, None if len(sys.argv) < 5 else sys.argv[4])
    #     if sys.argv[3] == "deleteuser":
    #         remove_user(db, None if len(sys.argv) < 5 else sys.argv[4])
    #     else:
    #         print("____________")
    # return

    if sys.argv[1] == "user":
        if sys.argv[2] == "register":
            register_user()
        if sys.argv[2] == "login":
            user = login(db)
            if user is None:
                print("Wrong credentials!")
                return
        if sys.argv[2] == "list":
            list_all_users(db)
        if sys.argv[2] == "findone":
            find_user_by_login(db, None if len(sys.argv) < 5 else sys.argv[4])
        if sys.argv[2] == "deleteuser":
            remove_user(db, None if len(sys.argv) < 5 else sys.argv[4])

    if sys.argv[1] == "room":
        user = login(db)
        if user is None:
            print("Wrong credentials!")
            return
        if sys.argv[2] == "create":
            create_room(db, user)
    # else:
    #         print("_________")
    return


def register_user():
    login = input("Login:")
    password = getpass.getpass("Password:")
    user_service.create_user(login, password)


@run.group("user")
@click.option("--login", required=True)
@click.password_option()
def login(db):
    login = input("Login:")
    password = getpass.getpass("Password:")
    return user_service.login(db, login, password)


def list_all_users(db):
    for user in user_service.get_all_users(db):
        print(user.login)


def find_user_by_login(db, name: str):
    name: str = input("Input name to find: ")
    print("Users with specified login: ")
    output = user_service.get_user_by_name(db, name)
    print(output[0])


def remove_user(db, nametodelete: str):
    nametodelete: str = input("Input name to delete: ")
    return user_service.remove_user(db, nametodelete)


def create_room(db, user):
    room_id = input("Input room id: ")
    room_service.create_room(db, room_id, user.login, getpass.getpass('Room password: '))


if __name__ == '__main__':
    run()
