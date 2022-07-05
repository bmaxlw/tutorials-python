from datetime import datetime
import time

# Outer function <track_execution_time> returns inner function <track> ...
# Inner function <track> takes *args which are passed through the function-variable ...
def track_execution_time(func):
    def track(*args): # both *args & **kwargs might be used as arguments for the inner function ...
        st = datetime.now()
        func(*args)
        et = datetime.now()
        print(f'Start: {st}\nStop: {et}\nDiff: {et-st}')
    # no execution of <track> inside the parent function, it is just returned ...
    return track

def count_to_x(x):
    for i in range(1, x + 1):
        print(i)
        time.sleep(1)

# ...
# tracker = track_execution_time(count_to_x)
# tracker(5)
# track_execution_time(count_to_x, x=5)()
# ...

# Rewritten to the @-based syntax
def track_execution_time_2(func):
    def track(*args):
        st = datetime.now()
        func(*args)
        et = datetime.now()
        print(f'Start: {st}\nStop: {et}\nDiff: {et-st}')
    return track

@track_execution_time_2
def count_to_x_2(x):
    for i in range(1, x + 1):
        print(i)
        time.sleep(1)

# count_to_x_2(5)

# With the return statement ...
def track_execution_time_3(func):
    def track(*args) -> str:
        st = datetime.now()
        func(*args)
        et = datetime.now()
        return f'Start: {st}\nStop: {et}\nDiff: {et-st}'
    return track

@track_execution_time_3
def count_to_x_3(x):
    for i in range(1, x + 1):
        print(i)
        time.sleep(1)

# print(count_to_x_3(5))