import functions as f
import functools as ft
import random as rnd
import time
import threading as th
from abc import ABC, abstractmethod

# Lambda basics
# get_email = lambda first_name, last_name: f'{first_name}.{last_name}@intermedia.com'.lower()
# check_login_password = lambda login, password: True if len(login) >= 5 and len(password) >= 10 else False
# get_sum = lambda *numbers: sum(numbers)
# get_sum_json = lambda total=0, **_json_: (for key, value in _json_ if value != 0: 'x')
get_gross_price = lambda prices: round(prices * 1.15, 2)
get_net_price = lambda prices: round(prices / 1.15, 2)

net = [14.99, 7.99, 15.99, 11.99, 8.99, 7.75]


def get_chosen_price(prices, x='g'):
    get_gross_price = lambda prices: round(prices * 1.15, 2)
    get_net_price = lambda prices: round(prices / 1.15, 2)
    if x == 'g':
        gross_price = tuple(map(get_gross_price, prices))
        return gross_price
    elif x == 'n':
        net_price = tuple(map(get_net_price, prices))
        return net_price
    else:
        return None


print(get_chosen_price(net, 'g'))