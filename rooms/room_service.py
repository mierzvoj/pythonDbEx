from getpass import getpass
from typing import List

import bcrypt as bcrypt

from database.database import Database

db = Database()


def create_room(db: Database, owner_id: str, password: str):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    db.insertIntoRooms(room_id=1, owner_id=owner_id, password=password)
