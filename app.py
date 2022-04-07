import functions as f
import functools as ft
import random as rnd
import time
import threading as th
from abc import ABC, abstractmethod
import datetime as dt

username = 'Admin'
user_password = '123456'
db = 'CustomerApp'

status = f.sql_server_connect(db).execute(
            f"SELECT ID FROM Users WHERE "
            f"Username = '{username}' AND Password = '{user_password}';"
        ).fetchone()

print(status)


















