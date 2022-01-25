import datetime as dt
import time
import requests as rq
import json
import functions as f
import random as rnd
import os
import shutil as sh

route = input('C R U D: ').upper()
if route == 'C':
    f.Customer(first_name=input('FirstName: '),
               last_name=input('LastName: '),
               phone_number=input('PhoneNumber: '),
               email_address=input('PhoneNumber: ')) \
        .create_customer()
elif route == 'R':
    f.Customer(customer_id=int(input('CustomerID: ')))\
        .read_customer()
elif route == 'U':
    f.Customer(customer_id=int(input('CustomerID: ')),
               first_name=input('FirstName: '),
               last_name=input('LastName: '),
               phone_number=input('PhoneNumber: '),
               email_address=input('PhoneNumber: ')) \
        .update_customer()
elif route == 'D':
    f.Customer(customer_id=int(input('CustomerID: ')))\
        .delete_customer()
else:
    pass










