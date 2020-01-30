from guppy import hpy
import timeit

start = timeit.default_timer()
h = hpy()


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


#@memoize #Comment this line for test
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print("fib 25 : {}".format(fib(25)))
print("memory consumption : {}".format((h.heap()).size))
print("Time from start : {}".format(timeit.default_timer() - start))

repeats =1000

time = timeit.Timer('fib(25)', 'from __main__ import fib')
sec = time.timeit(repeats)/repeats
print("mean time for the fib funciton : {}".format(sec))