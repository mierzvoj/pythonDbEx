import os
import sqlite3 as mdb
from sys import argv
from os import getenv
from sqlite3 import Error

from rooms.room_model import Room
from users.user_model import User
from pathlib import Path
import os


class Database:
    # path = os.path.abspath(os.getcwd())
    # databasePath = (os.path.abspath("users.db"))

    def __init__(self):
        self.conn = mdb.connect("users.db")
        self.conn.execute("pragma foreign_keys")
        self.cur = self.conn.cursor()
        self.user = User
        self.room = Room
        self.login = None
        self.password = None
        self.path = os.path.abspath(os.getcwd())
        self.logintofind = None

    def chk_conn(self):
        try:
            self.cursor()
            return True
        except Exception as ex:
            return False
    myconn = mdb.connect("users.db")
    if(chk_conn(myconn)):
        print("Database connected")
    else:
        print("Database connection failed")


    def createTableUsers(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
        user_id integer PRIMARY KEY,
        login text NOT NULL UNIQUE,
        password text NOT NULL,
        room_id integer,
        FOREIGN KEY (room_id)
            REFERENCES rooms (room_id)
        )
        ''')

    def createTableRooms(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
        room_id integer PRIMARY KEY,
        password text NOT NULL,
        owner_id integer NOT NULL
        )
        ''')

    def insertIntoUsers(self, login, password):
        conn = mdb.connect("users.db")
        cur = conn.cursor()
        cur.execute(f'INSERT OR IGNORE INTO users(login, password) VALUES(\"{login}\", \"{password}\")')
        conn.commit()
        conn.close()

    def find_in_db(self, login, password):
        conn = mdb.connect("users.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        check = cur.fetchall()
        # print(check)
        items = [i for i in check if login in i]
        return items[0] if items else None

    def find_all_in_db(self):
        print("list of  all Users: ")
        conn = mdb.connect("users.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        check = cur.fetchall()
        # print(check)
        return check

    def find_name_in_db(self, logintofind):
        print("List of all Users with specified name: ")
        conn = mdb.connect("users.db")
        cur = conn.cursor()
        sql = 'SELECT login FROM users where login=?;'
        cur.execute(sql, (logintofind,))
        check = cur.fetchall()
        print(check)
        return check[0] if check else None

    def remove_from_db(self, logintodelete):
        conn = mdb.connect("users.db")
        cur = conn.cursor()
        cur.execute('DELETE FROM users WHERE login=\"{logintodelete}\";')
        print("User deleted")

        def insertIntoRooms(self, one_user=None):
            self.cur.execute(
                "INSERT INTO rooms (password, owner_id) VALUES (\"password\", {}) RETURNING *".format(one_user[0]))
            created_room = self.cursor.fetchone()

        def selectFromUsers(self):
            self.cur.execute("SELECT * FROM users")
            all_users = self.cursor.fetchall()
            self.cur.execute("SELECT * FROM users WHERE login = \"A\"")
            one_user = self.cursor.fetchone()

        def remove_from_rooms(self, param, param1):
            pass

        def remove_from_users(self, param, param1):
            pass

        def find_all_users(self, param):
            pass

        def find_all_rooms(self, param):
            pass

        def close(self):
            self.conn.close()
