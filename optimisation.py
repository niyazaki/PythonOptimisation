import timeit

numbers0 = [n for n in range(10)]

numbers1 = [n for n in range(1000)]

numbers2 = [n for n in range(10000)]

numbers3 = [n for n in range(100000)]


def computeFor(n): 
    result = 0

    for i in n:
        result += i

    return result

def computeWhile(n):
    result = 0
    i = 0

    while i < len(n):
        result += n[i]
        i +=1

    return result

def computeSum(n):
    result = sum(n)

    return result

repeats = 1000

for i in range(4) :
    
    tFor = timeit.Timer('computeFor(numbers{})'.format(i), 'from __main__ import computeFor, numbers{}'.format(i))
    secFor = tFor.timeit ( repeats ) / repeats
    print ("{} : {} seconds". format ("for", secFor))

    tWhile = timeit.Timer('computeWhile(numbers{})'.format(i), 'from __main__ import computeWhile, numbers{}'.format(i))
    secWhile = tWhile.timeit ( repeats ) / repeats
    print ("{} : {} seconds". format ("while", secWhile))

    tSum = timeit.Timer('computeSum(numbers{})'.format(i), 'from __main__ import computeSum, numbers{}'.format(i))
    secSum = tSum.timeit ( repeats ) / repeats
    print ("{} : {} seconds". format ("sum", secSum))
