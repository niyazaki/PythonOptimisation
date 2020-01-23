import timeit

numbers = list(i*2 for i in range(1000))


def iterate1(a):
    list = []
    for i in range(len(a)):
        list.append((i, a[i]))
    return list


def iterate2(a):
    enumerateNumbers = enumerate(a)
    return list(enumerateNumbers)


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

# print(iterate1(numbers))
# print(iterate2(numbers))