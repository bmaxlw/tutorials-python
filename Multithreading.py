import functions as f
import functools as ft
import random as rnd
import time
import threading as th
from abc import ABC, abstractmethod
import datetime as dt

print('Main thread started:', x := dt.datetime.now())  # <= main thread


def f_a():
    time.sleep(1)
    print('Thread 2: f_a finished')


def f_b():
    time.sleep(2)
    print('Thread 3: f_b finished')


def f_c():
    time.sleep(3)
    print('Thread 4: f_c finished')


a = th.Thread(target=f_a)
b = th.Thread(target=f_b)
c = th.Thread(target=f_c)

print(f'Enumeration #1: {th.enumerate()}')  # <= only main thread enumerated
print(f'Active count #1: {th.active_count()}\n')  # <= active count == 1 since additional threads are not launched yet

a.start()  # <= 2nd thread initialized
b.start()  # <= 3rd thread initialized
c.start()  # <= 4th thread initialized

print(f'Enumeration #2: {th.enumerate()}')  # <= four threads enumerated
print(f'Active count #2: {th.active_count()}\n')  # <= active count == 4 since additional threads are already launched

a.join()  # join to the main thread makes main thread to wait until additional will be executed
print(f'Enumeration #3: {th.enumerate()}')  # <= 2nd thread is already killed => 3 remained
print(f'Active count #3: {th.active_count()}\n')  # <= active count == 3
b.join()
print(f'Enumeration #4: {th.enumerate()}')  # <= 3rd thread is already killed => 2 remained
print(f'Active count #4: {th.active_count()}\n')  # <= active count == 2
c.join()
print(f'Enumeration #5: {th.enumerate()}')  # <= 4th thread is already killed => main remained only
print(f'Active count #5: {th.active_count()}\n')  # <= active count == 1 (main)
print('Main thread executed:', y := dt.datetime.now())
print(y - x)

print(f'Enumeration #6: {th.enumerate()}')  # <= only main thread enumerated
print(f'Active count #6: {th.active_count()}')  # <= active count == 1 since all additional threads are already killed





