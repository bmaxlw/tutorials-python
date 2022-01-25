import math
import random
import os
from datetime import datetime as dt


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


# [24.01.22]: Takes:
#             > file_name_pattern => e.g.: '.txt'
#             > src_dir           => e.g.: 'C:/Users/user/Desktop/src_dir'
#             > tgt_dir           => e.g.: 'C:/Users/user/Desktop/tgt_dir'
#             Moves files with stated pattern from src_dir to tgt_dir and create log file to track changes
def move_specified_files(file_name_pattern, src_dir, tgt_dir):
    count_files = 0
    try:
        while True:
            for roots, folders, files in os.walk(src_dir):
                for file in files:
                    if file.endswith(file_name_pattern):
                        os.replace(f'{src_dir}/{file}', f'{tgt_dir}/{file}')
                        count_files += 1
                    else:
                        pass
                with open(f'{src_dir}/log.txt', 'a') as log_file:
                    log_file.write(f'\n{count_files} files uploaded: {dt.now()}')
                input('Done...')
    except FileNotFoundError:
        pass


# [22.01.22]: Simple constructor + function sample
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def show_credentials(self):
        return f'{self.first_name} {self.last_name}'
