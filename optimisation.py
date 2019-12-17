import timeit
import matplotlib.pyplot as plt

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
yFor, yWhile, ySum =  [],[],[]
x = [len(numbers0), len(numbers1), len(numbers2), len(numbers3)]
for i in range(4) :

    tFor = timeit.Timer('computeFor(numbers{})'.format(i), 'from __main__ import computeFor, numbers{}'.format(i))
    secFor = tFor.timeit ( repeats ) / repeats
    print ("{} : {} seconds". format ("for", secFor))
    yFor.append(secFor)

    tWhile = timeit.Timer('computeWhile(numbers{})'.format(i), 'from __main__ import computeWhile, numbers{}'.format(i))
    secWhile = tWhile.timeit ( repeats ) / repeats
    print ("{} : {} seconds". format ("while", secWhile))
    yWhile.append(secWhile)

    tSum = timeit.Timer('computeSum(numbers{})'.format(i), 'from __main__ import computeSum, numbers{}'.format(i))
    secSum = tSum.timeit ( repeats ) / repeats
    print ("{} : {} seconds". format ("sum", secSum))
    ySum.append(secSum)

plt.xlabel("Size of array")
plt.ylabel("Time (s)")


plt.plot(x,yFor, label ="f1 : For" )
plt.plot(x,yWhile, label ="f2 : While ")
plt.plot(x,ySum, label ="f3 : Sum" )
plt.legend(loc='best')
plt.show()