__author__ = 'Kalyan'

from placeholders import *


profiling_timeit = '''
Python also gives a helpful timeit module that can be used for benchmarking a given piece of code

Reading material:
 http://docs.python.org/3/library/timeit.html
 http://stackoverflow.com/questions/8220801/how-to-use-timeit-correctly
 http://www.dreamincode.net/forums/topic/288071-timeit-module/

Try out on sample code snippets from above links on your own before you get to the assignment.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit7_conversion_methods.py using timeit in this assignment.

for each value of count, execute the method 5 times using timeit and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

'''

from unit8_conversion_methods import *
import timeit

def profile_timeit():
    for i in range(1,5):
        l=[]
        for j in range(5):
            t=timeit.Timer("numbers_string1(10**"+str(i)+")",'''from unit8_conversion_methods import numbers_string1''').timeit(number=100)
            l.append(t)
        print('numbers_string1, count = ',10**i,', min = ',min(l),', actuals = ',l)
    for i in range(1, 5):
        l = []
        for j in range(5):
            t = timeit.Timer("numbers_string2(10**" + str(i) + ")",
                             '''from unit8_conversion_methods import numbers_string2''').timeit(number=100)

            l.append(t)
        print('numbers_string2, count = ', 10 ** i, ', min = ', min(l), ', actuals = ', l)
    for i in range(1, 5):
        l = []
        for j in range(5):
            t = timeit.Timer("numbers_string3(10**" + str(i) + ")",
                             '''from unit8_conversion_methods import numbers_string3''').timeit(number=100)

            l.append(t)
        print('numbers_string3, count = ', 10 ** i, ', min = ', min(l), ', actuals = ', l)
    for i in range(1, 5):
        l = []
        for j in range(5):
            t = timeit.Timer("num_strings4(10**" + str(i) + ")",
                             '''from unit8_conversion_methods import num_strings4''').timeit(number=100)

            l.append(t)
        print('num_strings4, count = ', 10 ** i, ', min = ', min(l), ', actuals = ', l)


# write your findings on what you learnt about timeit, measuring perf and how the results here compare to
# values in assignment1
summary = '''
    numbers_string2

'''

if __name__ == "__main__":
    profile_timeit()
