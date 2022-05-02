import os
import sqlite3
from sys import argv
from os import getenv
from sqlite3 import Error

from rooms.room_model import Room
from users.user_model import User


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.conn.execute("pragma foreign_keys")
        self.cur = self.conn.cursor()
        self.user = User
        self.room = Room

    def get_database(self):
        print("init")
        print(sqlite3.version)

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

    def insertIntoUsers(self):
        self.cur.execute("INSERT OR IGNORE INTO users VALUES(\"login\", \"password\")")
        self.conn.commit()
        self.conn.close()

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
