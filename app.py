import functions as f
import functools as ft
import random as rnd
import time
import threading as th
from abc import ABC, abstractmethod


class UserPattern(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class User(UserPattern):
    def go(self):
        print('GO')


class User2(UserPattern):
    def stop(self):
        print('STOP')


u = User()
u.go()