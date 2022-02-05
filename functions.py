import math
import random
import os
from datetime import datetime as dt
import pyodbc as db
from abc import ABC, abstractmethod
import functools as ft


# [22.01.22]: Takes number and power it should
#             be raised to. Returns the powered value.
def power(value, to_power):
    return math.pow(value, to_power)


# [22.01.22]: Takes a string with an email
#             and returns domain name of given email
def get_domain(string):
    x = str(string).find('@')
    return string[x:]


# [22.01.22]: Takes params for <get_evens_odds>
def get_params():
    start = int(input('x: '))
    stop = int(input('y: '))
    return [start, stop]


# [22.01.22]: Takes an input of two integers (start/stop) and returns
#             two lists with evens and odds in range of those two integers
def get_evens_odds(start, stop):
    evens_list = []
    odds_list = []
    try:
        for value in range(start, stop):
            if value % 2 != 0:
                odds_list.append(value)
            else:
                evens_list.append(value)
        return f'Evens: {evens_list} \nOdds: {odds_list}'
    except TypeError:
        return 'Incorrect input. Enter only integer values.'


# [22.01.22]: Takes as input any list with duplicates
#             and returns a sorted list without duplicates
def remove_duplicates(input_list):
    return list(set(input_list))


# [22.01.22]: Takes a number of prices and returns their total
def get_total(self, *prices):
    total = 0
    for price in prices:
        total += price
    return total


# [22.01.22]: Takes *args => True if two equal
def check_equal(*args):
    return args[0] == args[1]


# [23.01.22]: Takes **kwargs => incremented **kwargs pairs
#             Example: increment_rates(usd=27.5, eur=30.5,
#             gbp=32.5, increment=1.25)
def increment_rates(**rates):
    for key, value in rates.items():
        if key == 'increment':
            continue
        else:
            print(f"{key} > {value * rates['increment']}")


# [22.01.22]: Takes two lists/sets/tuples, compares them
#             and returns two lists with elements:
#             1) the <a> has, <doesn't>;
#             2) both <a> and <b> have in common;
def check_diff_inter(a, b):
    return f'Different: {list(set(a).difference(b))}\n' \
           f'Common:    {list(set(a).intersection(b))}'


# [23.01.22]: Converts input integer to binary
def to_binary(number):
    return "{:b}".format(number)


# [23.01.22]: Returns True if number == randint in range(x, y)
def guess(x, y, number):
    return number == random.randint(x, y)


# [23.01.22]: Returns a random password with lower/upper case letters and digits
def get_random_password(string_length):
    try:
        string = ''
        lower_cases = 'abcdefghigklmnopqrstuvwxyz'
        upper_cases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digit_signs = '1234567890!&?*$#'
        while len(string) <= string_length:
            string += random.choice(lower_cases) + \
                      random.choice(upper_cases) + \
                      random.choice(digit_signs)
        return string
    except TypeError:
        return "Please, enter integer value as <string_length> only!"


# [23.01.22]: Takes a list of names, returns three random "winners"
def get_three_random_winners(names):
    random.shuffle(names)
    return f'First place: {names[0]}\nSecond place: {names[1]}\nThird place: {names[2]}'


# [23.01.22]: Takes path and defines whether it leads to a file or directory
#             or to None
def check_path(path):
    if os.path.exists(path) and os.path.isfile(path):
        return 'isFile'
    elif os.path.exists(path) and os.path.isdir(path):
        return 'isDirectory'
    else:
        return 'notExists'


# [23.01.22]: Takes path => creates txt => populates it with 10
#             20-digit length passwords from <get_random_password> function
def txt_go_pass(path):
    u_idx = str(dt.now())[0:16].replace(' ', '_').replace('-', '_').replace(':', '_')
    u_path = f"{path}" \
             f"{u_idx}.txt"
    counter = 0
    with open(u_path, 'a'):
        with open(u_path, 'w') as file:
            while counter < 10:
                file.write(f'{get_random_password(20)}\n')
                counter += 1


# [25.01.22]: Takes:
#             > file_name_pattern => e.g.: '.txt'
#             > src_dir           => e.g.: 'C:/Users/user/Desktop/src_dir'
#             > tgt_dir           => e.g.: 'C:/Users/user/Desktop/tgt_dir'
#             Moves files with stated pattern from src_dir to tgt_dir and create log file to track changes
#               if target folder contains file with the same name doesn't move it
def move_specified_files(file_name_pattern, src_dir, tgt_dir):
    count_files = 0
    try:
        while True:
            for roots, folders, files in os.walk(src_dir):
                for file in files:
                    if file.endswith(file_name_pattern):
                        if os.path.exists(f'{tgt_dir}/{file}'):
                            continue
                        else:
                            os.replace(f'{src_dir}/{file}', f'{tgt_dir}/{file}')
                            count_files += 1
                    else:
                        pass
            with open(f'{src_dir}/log.txt', 'a') as log_file:
                log_file.write(f'\n************************************************'
                               f'\n{count_files} file(s) uploaded: '
                               f'\nDate:    {dt.now()}'
                               f'\nFrom:    {src_dir}'
                               f'\nTo:      {tgt_dir}'
                               f'\nPattern: {file_name_pattern}'
                               f'\n************************************************')
                input('Done...')
                break
    except FileNotFoundError:
        pass


# [25.01.22]: Takes a tuple of file patterns + source and target paths and executes the
#              move_specified_files() function, iterating through the tuple of patterns
def feed_specified_files(iteration_tuple, src_dir, tgt_dir):
    for file_pattern in iteration_tuple:
        move_specified_files(file_pattern, src_dir, tgt_dir)


# [25.01.22]: Takes <server_name, database_name, service, trusted> to set up the SQL Server connection
def setup_sql_connection(server_name, database_name,
                         service='SQL Server', trusted='yes'):
    try:
        conn = db.connect(f'Driver={service};'
                          f'Server={server_name};'
                          f'Database={database_name};'
                          f'Trusted_Connection={trusted};')
        print(f'Connected to {database_name}!')
        return conn
    except:  # simplified exception handling
        print('Connection failed!')


# [25.01.22]: Simple console CRUD simulation
# (!) DELETE REDUNDANCY OF CONNECTIONS, VIOLATING DRY
class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, phone_number=None, email_address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address

    def setup_sql_connection_to_customers(self):
        return setup_sql_connection('DESKTOP-VU19ML5', 'pypy')

    # add a new customer to the database
    def create_customer(self):
        conn = Customer.setup_sql_connection_to_customers(self)
        conn.execute("INSERT INTO Customers"
                     "(FirstName, LastName, PhoneNumber, EmailAddress) "
                     f"VALUES('{self.first_name}', '{self.last_name}', "
                     f"'{self.email_address}', '{self.phone_number}')")
        conn.commit()
        conn.close()

    # get a certain customer from the database
    def read_customer(self):
        conn = Customer.setup_sql_connection_to_customers(self)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Customers WHERE ID = {self.customer_id}")
        for item in cursor:
            print(item)

    # get all customers from the database
    def read_customers(self):
        conn = Customer.setup_sql_connection_to_customers(self)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Customers")
        for items in cursor.fetchall():
            print(items)

    # update a certain customer in the database
    def update_customer(self):
        conn = Customer.setup_sql_connection_to_customers(self)
        conn.execute("UPDATE Customers"
                     f"SET FirstName = '{self.first_name}', LastName = '{self.last_name}',"
                     f"PhoneNumber = '{self.phone_number}', EmailAddress = '{self.email_address}'"
                     f"WHERE ID = {self.customer_id}")
        conn.commit()
        conn.close()

    # delete a certain customer from the database
    def delete_customer(self):
        conn = Customer.setup_sql_connection_to_customers(self)
        conn.execute(f"DELETE FROM Customers WHERE ID = {self.customer_id}")
        conn.commit()
        conn.close()

    # delete all customers from the database (table)
    def delete_customers(self):
        conn = Customer.setup_sql_connection_to_customers(self)
        conn.execute(f"TRUNCATE TABLE Customers")
        conn.commit()
        conn.close()


# [27.01.2022] Multilevel inheritance
class GrandFather:
    def __init__(self, full_name):
        self.full_name = full_name

    def set_username(self):
        return str(self.full_name[0] +
                   self.full_name[self.full_name.index(' '):])\
                   .lower().replace(' ', '.')


class Father(GrandFather):
    def __init__(self, full_name, age):
        super().__init__(full_name)  # full_name inherited from GrandFather
        self.age = age  # age added as instance variable


class Son(Father):
    def __init__(self, full_name, age, height):
        super().__init__(full_name, age)  # full_name and age inherited from Father
        self.height = height  # height added as instance variable


class GrandSon(Son):
    def __init__(self, full_name, age, height, weight):
        super().__init__(full_name, age, height)  # full_name, age and height inherited from Son
        self.weight = weight  # weight added as instance variable


# [27.01.2022] Multiple inheritance with constructor derivation
# Sample 1
class Mother:
    def __init__(self, eye_color):
        self.eye_color = eye_color


class Dad:
    def __init__(self, hair_color):
        self.hair_color = hair_color


class Child(Mother, Dad):
    def __init__(self, eye_color, hair_color):
        super(Mother, self).__init__(eye_color)
        super(Dad, self).__init__(hair_color)


# Sample 2
class UserPattern:
    def __init__(self, first_name, last_name, email, phone, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.location = location


class ManagementPattern():
    def __init__(self, access_level):
        self.access_level = access_level


class Guest(UserPattern):
    def __init__(self, first_name, last_name, email, phone, location):
        super().__init__(first_name, last_name, email, phone, location)


class User(UserPattern):
    def __init__(self, first_name, last_name, email, phone, location):
        super().__init__(first_name, last_name, email, phone, location)
        self.username = ''
        self.password = ''

    def set_username(self):
        self.username = str(f'{self.first_name.lower()}.{self.last_name.lower()}')
        return self.username

    def set_password(self):
        self.password = str(f'{get_random_password(15)}')
        return self.password

    def set_corporate_email(self):
        return str(f'{User.set_username(self)}@hsbc-{self.location}.com').lower()


class Admin(UserPattern, ManagementPattern):
    def __init__(self, first_name, last_name, email, phone, location, access_level):
        UserPattern.__init__(self, first_name, last_name, email, phone, location)
        ManagementPattern.__init__(self, access_level)
        self.password = ''

    def set_password(self):
        self.password = str(f'{get_random_password(25)}')
        return self.password


# [27.01.2022] Overriding
class Animal:
    def __init__(self, what):
        self.what = what

    def say(self):
        return f'Animal is saying: "{self.what}"'


class Dog(Animal):
    def __init__(self, what):
        super().__init__(what)

    def say(self):
        return f'Dog is barking: "{self.what}"'


# [27.01.2022] Methods chaining
# (!) self has to be returned to chain functions since it returns the object itself and thus
#     the next method can be chained to the previous one
class Driver:
    def __init__(self, name):
        self.name = name

    def turn_on_car(self):
        print(f'{self.name} turns on the car!')
        return self  # if void is stated 'None' is returned and chaining fails

    def drive_the_car(self):
        print(f'{self.name} drives a car!')
        return self  # if return str/float/int, etc => function cannot be chained

    def stop_the_car(self):
        print(f'{self.name} stops the car!')
        return self


# [29.01.2022] Abstract class
class User2(ABC):
    @abstractmethod
    def get_first_name(self):
        pass

    def get_last_name(self):
        pass


class Employee(User2):
    def __init__(self, full_name):
        self.full_name = full_name

    def get_first_name(self):
        idx = str(self.full_name).index(' ')
        return self.full_name[0:idx]

    def get_last_name(self):
        idx = str(self.full_name).index(' ') + 1
        return self.full_name[idx:]


# [30.01.2022] Takes total (by default = 0) and sums up the provided prices
# (!) Walrus used
def get_total_prices(total=0):
    while (price := input('> ')) != 'end':  # brackets with (price := input('> ')) are obligatory else: bool provided
        total += float(price)
    return round(total, 2)


# [31.01.2022]: Lambda
lambda_1 = lambda x: True if x >= 18 else False
lambda_2 = lambda x, y: True if x == y else False
lambda_3 = lambda x, y: True if x is y else False


# [03.02.2022] Higher order Functions
# 1) Takes other function as argument
class Employee:
    def __init__(self):
        self.__first_name = str()
        self.__last_name = str()

    def set_credentials(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_credentials(self):
        return self.__first_name, self.__last_name

    def create_user_account(self, get_credentials):  # takes a function as an argument
        creds = get_credentials()
        username = f'{creds[0][0:2]}{creds[1]}'.lower()
        email = f'{creds[0]}.{creds[1]}@corporate.com'.lower()
        return username, email  # returns a tuple


# 2) Returns a function
def increment_by(times):
    def get_data(dataset):  # takes an iterable as an argument
        result_set = list()
        for item in dataset:
            result_set.append(item * times)
        return result_set
    return get_data


def get_prices(prices):  # takes an iterable of prices
    def apply_rates(rate):
        result_prices = list()
        for item in prices:
            result_prices.append(round(item * (1 + float(rate)), 2))  # applies rates to each price
        return result_prices
    return apply_rates


# [03.02.2022] Describe iterable
def describe_data(dataset):
    x = float()
    for i in dataset:
        x += i
    return f'Min: {min(dataset)} ' \
           f'\nMax: {max(dataset)} ' \
           f'\nAvg: {round(x/len(dataset), 2)}'


# [03.02.2022] Describe iterable
def compare(a, b):
    if a is b:
        return True
    else:
        return False


# [04.02.2022] Sort and return any iterable
def sort_iterable(iterable, idx):
    sorted_iterable = sorted(iterable, key=lambda itr: itr[idx])
    return sorted_iterable


# [04.02.2022] Takes [[]] as <data> with values and increment each value is not str by <rate>
def increment_by(data, rate):
    x = list()
    for items in data:
        for item in items:
            if type(item) is not str:
                item *= rate
                x.append(item)
            else:
                continue
    return x


# [05.02.2022]
# <map>, <sort>, <filter> examples
#          name    age
names = [['James', 20],
         ['Amanda', 25],
         ['Peter', 18],
         ['Anna', 17]]


def filter_map_sort(iterable):
    iterable = list(filter(lambda x: x[1] > 18, iterable))  # filters records where age > 18
    iterable = list(map(lambda y: (y[0], y[1] + 1), iterable))  # applies +1 to each age
    iterable.sort(key=lambda z: z[1])  # sorts by age with lambda as key to it
    # iterable = sorted(iterable, key=lambda z: z[1])  # 2nd variant of sorting
    return iterable


# [05.02.2022]
# <reduce> examples (functools)
def cart_counter():
    idx = 3
    cart = list()
    while x := float(input('> ')):
        cart.append(x)
        if len(cart) >= idx:
            price = ft.reduce(lambda a, b: a + b, cart)
            print(f'The price is {round(price, 2)} EUR')
            qa = input('Proceed? Y/N: ').lower()
            if qa == 'y':
                idx += idx
                continue
            else:
                print(f'{price} EUR is the final price of your cart!')
                break


# [05.02.2022]
# takes <number>, returns its factorial
def get_factorial(number):
    iterable = list()
    while number > 0:
        iterable.append(number)
        number -= 1
    number = ft.reduce(lambda a, b: a * b, iterable)
    return number
