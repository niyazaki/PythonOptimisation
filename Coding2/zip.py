import timeit

numbers = list(range(1000))
double = list(i*2 for i in range(1000))


def iterate1(a, b):
    list = []
    for i in range(len(numbers)):
        list.append((numbers[i], double[i]))
    return list


def iterate2(a, b):
    zipped = zip(a, b)
    return list(zipped)


def iterFor():
    return iterate1(numbers, double)


def iterZip():
    return iterate2(numbers, double)


repeats = 1000
t1 = timeit.Timer('iterFor()', 'from __main__ import iterFor')
sec1 = t1.timeit(repeats)/repeats
t2 = timeit.Timer('iterZip()', 'from __main__ import iterZip')
sec2 = t2.timeit(repeats)/repeats
print('{} seconds'.format(sec1))
print('{} seconds'.format(sec2))
