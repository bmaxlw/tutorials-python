import math


# [22.01.22]: Takes number and power it should
# be raised to. Returns the powered value.
def power(value, to_power):
    return math.pow(value, to_power)


# [22.01.22]: Takes a string with an email
# and returns domain name of given email
def get_domain(string):
    x = str(string).find('@')
    return string[x:]


# [22.01.22]: Takes params for <get_evens_odds>
def get_params():
    start = int(input('x: '))
    stop = int(input('y: '))
    return [start, stop]


# [22.01.22]: Takes an input of two integers (start/stop) and returns
# two lists with evens and odds in range of those two integers
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
# and returns a sorted list without duplicates
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
# Example: increment_rates(usd=27.5, eur=30.5, gbp=32.5, increment=1.25)
def increment_rates(**rates):
    for key, value in rates.items():
        if key == 'increment':
            continue
        else:
            print(f"{key} > {value * rates['increment']}")


# [22.01.22]: Takes two lists/sets/tuples, compares them
# and returns two lists with elements:
# 1) the <a> has, <doesn't>;
# 2) both <a> and <b> have in common;
def check_diff_inter(a, b):
    return f'Different: {list(set(a).difference(b))}\n' \
           f'Common:    {list(set(a).intersection(b))}'


# [22.01.22]: Simple constructor + function sample
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def show_credentials(self):
        return f'{self.first_name} {self.last_name}'


# [23.01.22]: