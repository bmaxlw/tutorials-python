import math


# [22.01.21]: Takes number and power it should
# be raised to. Returns the powered value.
def power(value, to_power):
    return math.pow(value, to_power)


# [22.01.21]: Takes a string with an email
# and returns domain name of given email
def get_domain(string):
    x = str(string).find('@')
    return string[x:]


# [22.01.21]: Takes params for <get_evens_odds>
def get_params():
    start = int(input('x: '))
    stop = int(input('y: '))
    return [start, stop]


# [22.01.21]: Takes an input of two integers (start/stop) and returns
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


# [22.01.21]: Takes as input any list with duplicates
# and returns a sorted list without duplicates
def remove_duplicates(input_list):
    return list(set(input_list))


# [22.01.21]: Takes a number of prices and returns their total
def get_total(self, *prices):
    total = 0
    for price in prices:
        total += price
    return total


# [22.01.21]: Takes two lists/sets/tuples, compares them
# and returns a list with elements the <a> has, <doesn't>
def check_diff(a, b):
    return list(set(a).difference(b))





















