import functions as f
import functools as ft
import random as rnd
import time
import threading as th
from abc import ABC, abstractmethod
import datetime as dt


def ask():
    answer = input('> ').lower()
    if answer == 'yes':
        print('Correct!')
    else:
        print('Wrong!')


def wait():
    time.sleep(5)
    print('Your time is over!')



a = th.Thread(target=ask, daemon=True)
# b = th.Thread(target=wait)

a.start()
wait()
# b.start()


















