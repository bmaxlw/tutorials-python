import functions as f
import functools as ft
import random as rnd
import time
import threading as th
from abc import ABC, abstractmethod
import datetime as dt

db = 'CustomerApp'
username = 'A'
user_password = '1'

auth = 3
status = f.sql_server_connect(db).execute(
            f"SELECT TOP 1 ID FROM Users WHERE "
            f"Username = '{username}' AND Password = '{user_password}';"
        ).fetchall()
try:
    for i in status:
        auth = 1
except TypeError:
        auth = 0

if auth == 1:
    print(1)
else:
    print('hui')


















