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


def computeWhile(n):
    result = 0
    i = 0

    while i < len(n):
        result += n[i]
        i +=1

    return result

repeats = 1000
t = timeit.Timer('computeWhile([1,2,3,4,5])', 'from __main__ import computeWhile')
sec = t.timeit ( repeats ) / repeats
print ("{} seconds". format (sec))


def computeSum(n):
    result = sum(n)

    return result

repeats = 1000
t = timeit.Timer('computeSum([1,2,3,4,5])', 'from __main__ import computeSum')
sec = t.timeit ( repeats ) / repeats
print ("{} seconds". format (sec))
