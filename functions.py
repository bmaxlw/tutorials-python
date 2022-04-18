import math
import random as rnd
import os
from datetime import datetime as dt
import pyodbc as db
from abc import ABC, abstractmethod
import functools as ft
import smtplib
import numpy as np


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
                log_file.write(f'\n**********************************'
                               f'\n{count_files} file(s) uploaded: '
                               f'\nDate:    {dt.now()}'
                               f'\nFrom:    {src_dir}'
                               f'\nTo:      {tgt_dir}'
                               f'\nPattern: {file_name_pattern}'
                               f'\n**********************************')
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


# [27.01.2022]: Overriding
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


# [27.01.2022]: Methods chaining
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


# [29.01.2022]: Abstract (objects cannot be instantiated from abstract classes)
class User2(ABC):
    @abstractmethod
    def get_first_name(self):  # each abstract method is 'empty' and has to be overridden
        pass

    @abstractmethod
    def get_last_name(self):
        pass


class Employee(User2):
    def __init__(self, full_name):
        self.full_name = full_name

    def get_first_name(self):  # overriding of abstract methods
        idx = str(self.full_name).index(' ')
        return self.full_name[0:idx]

    def get_last_name(self):  # overriding of abstract methods
        idx = str(self.full_name).index(' ') + 1
        return self.full_name[idx:]


# [30.01.2022]: Takes total (by default = 0) and sums up the provided prices
# (!) Walrus used
def get_total_prices(total=0):
    while (price := input('> ')) != 'end':  # brackets with (price := input('> ')) are obligatory else: bool provided
        total += float(price)
    return round(total, 2)


# [31.01.2022]: Lambda
lambda_1 = lambda x: True if x >= 18 else False
lambda_2 = lambda x, y: True if x == y else False
lambda_3 = lambda x, y: True if x is y else False


# [03.02.2022]: Higher order functions either: 1) accept(s) function(s) as (an) argument(s)
#                                          or: 2) return(s) function(s)
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


# [03.02.2022]: Describe iterable
def describe_data(dataset):
    x = float()
    for i in dataset:
        x += i
    return f'Min: {min(dataset)} ' \
           f'\nMax: {max(dataset)} ' \
           f'\nAvg: {round(x/len(dataset), 2)}'


# [03.02.2022]: Checks if <a> IS <b>
def compare(a, b):
    if a is b:
        return True
    else:
        return False


# [04.02.2022]: Sort and return any iterable
def sort_iterable(iterable, idx):
    sorted_iterable = sorted(iterable, key=lambda itr: itr[idx])
    return sorted_iterable


# [04.02.2022]: Takes [[]] as <data> with values and increment each value is not str by <rate>
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


# [05.02.2022]: <map>, <sort>, <filter> examples
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


# [05.02.2022]: <reduce> examples (functools)
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


# [05.02.2022]: takes <number>, returns its factorial
def get_factorial(number):
    iterable = list()
    while number > 0:
        iterable.append(number)
        number -= 1
    number = ft.reduce(lambda a, b: a * b, iterable)
    return number


# [05.02.2022]: <list comprehension>
#                       Patterns:
#                       list = [expression for item in iterable] => [i for i in iterable] or ['sth' for i in iterable]
#                       list = [expression for item in iterable if conditional] => [i for i in iterable if ...]
#                       list = [expression if/else for item in iterable] => ['sth' if ... else ... for i in iterable]
# Takes <iterable> and <condition> as upper limit of True being fired
# makes a list comprehension to those below <condition> as False
# counts the ratio btn pos (True) and neg (False) in percentages
def ratio_pos_neg(iterable, condition):
    out = [False if item < condition else True for item in iterable]
    pos = out.count(True)
    neg = out.count(False)
    return f'{round(pos/len(out) * 100, 2)}% positive' \
           f'\n{round(neg/len(out) * 100, 2)}% negative'


# [06.02.2022]: <list comprehension> Takes an iterable as an argument and returns two lists with odds and evens
def sort_odd_even(iterable):
    evens = [even if (even % 2 == 0) else None for even in iterable]
    odds = [odd if (odd % 2 > 0) else None for odd in iterable]
    for e in evens:
        if e is None:
            evens.remove(e)
    for o in odds:
        if o is None:
            odds.remove(o)
    return f'Evens: {evens}\n Odds: {odds}'


# [08.02.2022]: <dictionary comprehension> Takes a dictionary with pattern {'key_name': float} and
# returns a string with two dictionaries presenting floats above and below avg of input params
# [Input sample]: rates = {'AAPL': 290.99, 'FB': 105.75, 'TSLA': 210.50, 'PTON': 221.99, 'AMD': 199.99, 'AMZN': 175.55}
def comp_d(dictionary):
    def get_avg():
        tot = 0
        for i in dictionary.values():
            tot += i
        return tot / len(dictionary)
    avg = get_avg()
    above_avg = {
        key: value for key, value in dictionary.items() if value > avg
    }
    below_avg = {
        key: value for key, value in dictionary.items() if value <= avg
    }
    return f'Average: {round(avg, 2)}\nAbove: {above_avg}\nBelow: {below_avg}'


# [09.02.2022]: Takes two iterables and <return type>. Returns zipped collection of stated type
def return_as(iter1, iter2, return_type='dict'):
    try:
        if return_type == 'dict':
            return dict(zip(iter1, iter2))
        elif return_type == 'tup':
            return tuple(zip(iter1, iter2))
        elif return_type == 'list':
            return list(zip(iter1, iter2))
        elif return_type == 'set':
            return set(zip(iter1, iter2))
        elif return_type == 'frozen':
            return frozenset(zip(iter1, iter2))
        else:
            return zip(iter1, iter2)
    except:
        print('Unexpected error!')

        
# [24.03.2022]: Sorting odds/evens to separate lists and removes duplicates
def odd_even(iterable):
    odds, evens = [], []
    for i in iterable:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return f'Odds: {list(set(odds))} \nEvens: {list(set(evens))}'


# [24.03.2022]: Compares two iterables and presents
# 1) what it1 has that it2 doesn't / 2) what it2 has that it1 doesn't
def compare_iterables(it1, it2):
    return f'{set(it1).difference(it2)}\n' \
           f'{set(it2).difference(it1)}'


# [25.03.22]: Takes dictionary of type {x: [a, b, c], y: [d, e, f]} returns rows as
# x y
# a d
# b e
# c f
def dictionary_to_table(dictionary):
    keys = []
    for key, value in dictionary.items():
        keys.append(key)
    for k in dictionary.keys():
        print(k, end=' ')
    print()
    for i in range(len(value)):
        for j in keys:
            print(dictionary[j][i], end=' ')
        print('')


# [27.03.22]: Inheritance + class variables + instance variables example
class User:
    domain_name = '@union.com'
    email_address = str()

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def assign_email_address(self):
        self.email_address = f'{self.f_name}.{self.l_name}' \
                             f'{self.domain_name}'.lower()


class Admin(User):
    admin_name = 'adm'
    admin_id = 11485596

    def change_email_address(self, target_user):
        target_user.email_address = \
            self.admin_name + str(self.admin_id) + target_user.domain_name


# [28.03.22]: Splits **kwargs into keys/values lists, returns as a string
def split_dict_to_lists(**inp_dict):
    keys, values = [], []
    for key, value in inp_dict.items():
        keys.append(key)
        values.append(value)
    return f'keys : {keys}\nvalues: {values}'


# [28.03.22]: Takes a number returns a binary
def to_binary(number):
    return '{:b}'.format(number)


# [28.03.22]: Takes rounds/return_lists (0 - not return lists, 1 - return numbers lists)
#             returns possibility breakdown out of rounds
def check_possibility(rounds=10, return_lists=0):
    cz, co, idx, z_list, o_list,  = 0, 0, 0, [], []
    while idx < rounds:
        for x in range(rounds):
            if rnd.randint(0, 1) == 0:
                cz += 1
            else:
                co += 1
        z_list.append(cz)
        o_list.append(co)
        cz, co = 0, 0
        idx += 1
    if return_lists == 1:
        return f'Zeros: {z_list}\n' \
               f'Ones: {o_list}\n' \
               f'AvgZeros: {round(sum(z_list)/rounds, 2)}\n' \
               f'AvgOnes: {round(sum(o_list)/rounds, 2)}'
    else:
        return f'AvgZeros: {round(sum(z_list)/rounds, 2)}\n' \
               f'AvgOnes: {round(sum(o_list)/rounds, 2)}'


# [29.03.22]: Takes tries/collection to iterate through collection
#             and return the % of each value (inside iteration) selection
def try_get(tries, *collection):
    choices, counts = [], {}
    for i in range(tries):
        # choices.append(collection.index(rnd.choice(collection)))
        choices.append(rnd.choice(collection))
    for e in collection:
        counts[e] = choices.count(e)
        # counts.append(f'{e}: {choices.count(e)}')
    for key, value in counts.items():
        counts[key] = f'{round((value / tries) * 100, 2)}%'
    return counts


# [29.03.22]: Takes different variables and converts them to int if possible
def check_inputs(*variables):
    ints = []
    for i in variables:
        try:
            x = int(i)
        except ValueError:
            continue
        except TypeError:
            continue
        else:  # if except is False, else is used to append
            ints.append(x)
        finally:  # finally is used in any case (if except is True/False)
            print(f'.', end='.')
    return f'\n{len(ints)}/{len(variables)} success' \
           f'\n{len(variables) - len(ints)}/{len(variables)} failure' \
           f'\n{ints}'


# [29.03.22]: Checks whether file(s) exist(s)
def check_file_exist(path, extension, *names):
    exists, not_exists = [], []
    for file in names:
        if os.path.exists(f'{path}/{file}.{extension}'):
            exists.append(file)
        else:
            not_exists.append(file)
    return f'(+): {exists}\n(-): {not_exists}'


# [29.03.22]: Gets total of floats from a text file
def get_total_out_of_file(path):
    with open(path, 'r') as file:
        raw, clean = file.read().split('\n'), []
        for i in raw:
            j = i.split(',')
            for k in j:
                try:
                    clean.append(float(k))
                except ValueError or TypeError:
                    continue
                except:
                    return False
    return sum(clean)


# [30.03.22]: MS SQL Connection
def sql_server_connect(database, server='5CD116MK2D',
                       driver='{ODBC Driver 17 for SQL Server}',
                       trusted='yes'):
    cursor = db.connect(f'DRIVER={driver};'
                        f'SERVER={server};'
                        f'DATABASE={database};'
                        f'Trusted_Connection={trusted};').cursor()
    return cursor


# [30.03.22]: MS SQL Extraction to txt
def sql_server_extract_data_to_txt(txt_path, source_database, select_statement):
    extraction = sql_server_connect(source_database).execute(select_statement).fetchall()
    with open(txt_path, 'a') as file:
        for i in extraction:
            file.write(f'{i}\n')


# [30.03.22]: OOP patterns
class Product:

    tax_rate = 1.15  # class variable

    def __init__(self, name, net_price):
        self.name = name  # instance variable
        self.net_price = net_price  # instance variable
        self.gross_price = round(net_price * self.tax_rate, 2)  # derived from instance + class variables

    def change_tax_rate(self, new_tax_rate):
        self.tax_rate = new_tax_rate  # changes the class variable
        self.gross_price = round(self.net_price * self.tax_rate, 2)  # changes var-s derived from class var

    def show_all(self):
        return self.name, self.net_price, self.gross_price


# [01.04.22]: Sorting using keys (lambdas) for [(a, b, c)] iterable types
def sort_iterable_by_key(iterable, index, reverse_status=False):
    key = lambda iterable: iterable[index]
    # iterable.sort(key=key, reverse=reverse_status) => for list type iterables
    sorted_iterable = sorted(iterable, key=key, reverse=reverse_status)  # for all iterables
    for i in sorted_iterable:
        print(i)


# [01.04.22]: Get either net/gross price from iterable prices with map func
def get_updated_prices1(prices, x='g'):
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


# [02.04.22]: Takes *args of strings, returns their lengths as list
def get_lengths_of_strings(*input_strings):
    lengths = [len(i) for i in input_strings if type(i) == str]
    return lengths


# [02.04.22]: Takes *args of integers/floats, returns the dynamics of differences
#             (e.g.: takes [1, 2, 4] and returns [1, 2] since 2 - 1 = 4 / 4 - 2 = 2
#                or: takes [3, 2, 1] and returns [-1, -1]).
#             On the basis of that dynamics returns the ratio of pos/neg/neu dynamics
#             as well as a percentage ratio of it.
def display_dynamics(input_iterable):  # or *input_iterable
    try:
        start, return_list, percentage_list = 0, [], []
        for item in input_iterable:
            return_list.append(round(item - start, 2))
            percentage_list.append(round((item - start) / item, 2) * 100)
            start = item
        pos = list(filter(lambda pos_values: pos_values > 0, return_list))
        neu = list(filter(lambda neu_values: neu_values == 0, return_list))
        neg = list(filter(lambda neg_values: neg_values < 0, return_list))
        return f'Dynamics: {return_list[1:]}\n' \
               f'Percents: {percentage_list[1:]}\n' \
               f'Pos: {round((len(pos) - 1) / (len(input_iterable) - 1), 3)}\n' \
               f'Neg: {round(len(neg) / (len(input_iterable) - 1), 3)}\n' \
               f'Neu: {round(len(neu) / (len(input_iterable) - 1), 3)}'
    except TypeError:
        return 'Only integers/floats are allowed as input!'


# [02.04.22]: Takes rate and products as kwargs, returns incremented values
#             using dictionary comprehension
def increment_by_rate(rate=1.15, **products):
    taxed = {key: value * rate for (key, value) in products.items()}
    return taxed


# [02.04.22]: List comprehension patterns
# list_comp_lambda = lambda inp_iter:
# lc_list = [1, 2, 3, 4, -1, -2, -3, -4]  # test input list
# b1 = [i for i in lc_list]  # 1st variant
# print(b1)
# b2 = ['odd' if i % 2 != 0 else 'even' for i in lc_list]  # 2nd variant
# print(b2)
# b3 = [i for i in lc_list if i == abs(i)]  # 3rd variant
# print(b3)
# get_incremented1 = lambda c_iter, x: (c_iter[0] + x, c_iter[1] + x, c_iter[2] + x)
# complex_prices = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
# b4 = [get_incremented1(i, 100) for i in complex_prices]  # not only lambda but usual function might be used
# print(b4)
# b5 = [abs(i) for i in lc_list]
# print(abs_list)


# [02.04.22]: Dictionary comprehension patterns
# output = {key: value for key, value in products.items()}  # full dict comprehension without conditions
# output = {key: value for key, value in products.items() if value > 10}  # dict comprehension with if statement
# output = {key: 'more 5' if value > 5 else 'less 5' for key, value in products.items()}  # if/else statement for value
# output = {'x' if key.startswith('C') else 'y': value for key, value in products.items()} # if/else statement for key
# output = {key: check_price(value) for key, value in products.items()}  #function used as value in dict comp.


# [02.04.22]: Basic lambdas
# get_email = lambda first_name, last_name: f'{first_name}.{last_name}@intermedia.com'.lower()
# check_login_password = lambda login, password: True if len(login) >= 5 and len(password) >= 10 else False
# get_sum = lambda *numbers: sum(numbers)
# get_sum_json = lambda total=0, **_json_: (for key, value in _json_ if value != 0: 'x')
# get_gross_price = lambda prices: round(prices * 1.15, 2)
# get_net_price = lambda prices: round(prices / 1.15, 2)
# get_gross_price2 = lambda iterable: (iterable[0], round(iterable[1] * 1.15, 2))
# if_js_in_position = lambda itr: 'JS' in itr[1] or 'js' in itr[1]


# [03.04.22]: Zip function sample. Takes three iterables, returns zipped
#             e.g.: ['Max', 'Jack'], [10, 20], ['A', 'B'] => ('Max', 10, 'A'), ('Jack', 20, 'B')
def get_zipped(a, b, c):
    return tuple(zip(a, b, c))  # zip takes as many args as needed


# [03.04.22]: if __name__ == '__main__'
# if code is imported and run from another module it was created in then __name__ == name of the module
# if code is run with the module it is created in (not imported) then __name__ == __main__


# [12.04.22]: Sends email
def send_email(sender, receiver, password, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    message = f'Subject: {subject}\n{body}'
    try:
        server.login(sender, password)
        print('Successfully logged in...')
    except:
        print('Error while signing in...')
    try:
        server.sendmail(sender, receiver, message)
        print('Email has been sent!')
    except:
        print('Error while sending an email!')


# [13.04.22]: .exe
# pyinstaller -F -w -i loader_logo.ico main.py

# [18.04.22]: Numpy
def run_numpy_training_function():
    np_array1 = np.array([1, 2, 3, 4, 5])
    np_array2 = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    np_array3 = np.array([10, 20, 30, 40, 50])
    np_array4 = np.arange(4)
    py_list1 = [1, 2, 3, 4, 5]

    # Case №1:
    print('Case №1:')
    np_array1 += 10  # += updates original object
    print(np_array1)
    print(np_array1 + 10)  # + doesn't update original object
    print()

    # Case №2:
    print('Case №2:')
    print(np_array2 + np_array3)
    np_array2 += np_array3
    print(np_array2)
    print()

    # Case №3:
    print('Case №3:')
    print(np_array4[[True, True, False, False]])  # select first two but not last two


