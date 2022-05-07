from getpass import getpass
from typing import List

import bcrypt as bcrypt

from database.database import Database
from rooms.room_model import Room

db = Database()


def create_room(db: Database, room_id: str, owner_id: str, password: str):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    db.insertIntoRooms(room_id=room_id, owner_id=owner_id, password=password)


def get_room(db: Database, room_id: str):
    db_room = db.find_room_in_db(room_id)
    if db_room is None:
        return None
    return Room(id=db_room[1], password=db_room[2], room_id=db_room[3])

