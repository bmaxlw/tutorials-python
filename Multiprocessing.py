import datetime
from multiprocessing import Process, cpu_count
import time
import threading as th

# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

# Multithreading - because of GIL (which allows only one thread to hold the control
#                  of the Python interpreter at any one time) tasks are taking turns and not fully parallel
# Multiprocessing - tasks are fully parallel


def count(num):
    # start = datetime.datetime.now()
    c = 0
    while c < num:
        c += 1
    # end = datetime.datetime.now()
    # print('Execution time: ', end - start)


if __name__ == '__main__':

    # Single
    start1 = datetime.datetime.now()
    count(1000000000)
    end1 = datetime.datetime.now()
    print('Single thread:', end1 - start1)

    # Multithreading
    start2 = datetime.datetime.now()
    a = th.Thread(target=count, args=(500000000,))
    b = th.Thread(target=count, args=(500000000,))
    a.start()
    b.start()
    a.join()
    b.join()
    end2 = datetime.datetime.now()
    print('Multithreading:', end2 - start2)

    # Multiprocessing
    start3 = datetime.datetime.now()
    x = Process(target=count, args=(500000000,))
    y = Process(target=count, args=(500000000,))
    x.start()
    y.start()
    x.join()
    y.join()
    end3 = datetime.datetime.now()
    print('Multiprocessing:', end3 - start3)

#  Batch #1:
#  Single thread:   0:00:32.750865
#  Multithreading:  0:00:30.695633
#  Multiprocessing: 0:00:18.015830
