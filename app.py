import functions as f
import functools as ft
import random as rnd
import time
import threading as th


def timer():
    sec = 1
    while True:
        print(f'App is running for {sec} second(s)')
        time.sleep(1)
        sec += 1


def get_input():
    return input('Type something: \n')


th.Thread(target=get_input).start()
th.Thread(target=timer, daemon=True).start()

