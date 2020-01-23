import timeit

def computeSum(n):
    result = sum(n)

    return result

repeats = 1000
t = timeit.Timer('computeSum([1,2,3,4,5])', 'from __main__ import computeSum')
sec = t.timeit ( repeats ) / repeats
print ("{} seconds". format (sec))
