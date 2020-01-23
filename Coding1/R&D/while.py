import timeit

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
