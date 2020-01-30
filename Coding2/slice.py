import timeit

numbers = list(range(100000))


def iterate1(a):
    list = []
    for i in range(len(a)//2):
        list.append(a[i])
    return list


def iterate2(a):
    return a[slice(len(a)//2)]


def test1():
    return iterate1(numbers)


def test2():
    return iterate2(numbers)


repeats = 1000
t1 = timeit.Timer('test1()', 'from __main__ import test1')
sec1 = t1.timeit(repeats)/repeats
t2 = timeit.Timer('test2()', 'from __main__ import test2')
sec2 = t2.timeit(repeats)/repeats
print('{} seconds'.format(sec1))
print('{} seconds'.format(sec2))
