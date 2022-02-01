import datetime as dt
import time
import requests as rq
import json
import functions as f
import random as rnd
import os
import shutil as sh

route = input('Create Remove Update Delete: ').upper()
if route == 'Create':
    f.Customer(first_name=input('FirstName: '),
               last_name=input('LastName: '),
               phone_number=input('PhoneNumber: '),
               email_address=input('PhoneNumber: ')) \
        .create_customer()
elif route == 'Remove':
    f.Customer(customer_id=int(input('CustomerID: ')))\
        .read_customer()
elif route == 'Update':
    f.Customer(customer_id=int(input('CustomerID: ')),
               first_name=input('FirstName: '),
               last_name=input('LastName: '),
               phone_number=input('PhoneNumber: '),
               email_address=input('PhoneNumber: ')) \
        .update_customer()
elif route == 'Delete':
    f.Customer(customer_id=int(input('CustomerID: ')))\
        .delete_customer()
else:
    pass










