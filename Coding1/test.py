import timeit
numbers = [n for n in range(1000)]


def repeatFct(fct, numbers,  repeats):
    t = timeit.Timer("{}(numbers{})".format(fct, numbers), "from __main__ import {}, numbers{}".format(fct, numbers))
    sec = t.timeit(repeats)/repeats
    print("{} : {} seconds".format(fct, sec))


def computeFor(n):
    result = 0

    for i in n:
        result += i

    return result


list1 = [1, 2, 3, 4, 5, 6, 7]


repeatFct("computeFor", list1,  1000)
