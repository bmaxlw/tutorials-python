import functions as f
import functools as ft
import random as rnd
import time
import threading as th
from abc import ABC, abstractmethod
import datetime as dt
import smtplib
import numpy as np
import requests
import json
import time

# while True:
#     response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#     data = response.text
#     json_data = json.loads(data)
#     print(json_data)
#
#     utc_time = json_data['time']['updated']
#     usd_rate = str(json_data['bpi']['USD']['rate'].replace(',', ''))
#     eur_rate = str(json_data['bpi']['EUR']['rate'].replace(',', ''))
#     gbp_rate = str(json_data['bpi']['GBP']['rate'].replace(',', ''))
#
#     query = f"INSERT INTO BTC_rate(utc_time, BTC_USD, BTC_EUR, BTC_GBP) " \
#             f"VALUES('{utc_time}', {usd_rate}, {eur_rate}, {gbp_rate});"
#     f.
#     time.sleep(61)

