import timeit

def computeFor(n): 
    result = 0

    for i in n:
        result += i

    return result

repeats = 1000
t = timeit.Timer('computeFor([1,2,3,4,5])', 'from __main__ import computeFor')
sec = t.timeit ( repeats ) / repeats
print ("{} seconds". format (sec))
