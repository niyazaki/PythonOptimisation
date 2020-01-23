import timeit

start = timeit.default_timer()
data_list = list(range(1000000))
new_list = []

for i in data_list:
    new_list.append(i)

stop = timeit.default_timer()
print("Time from start : {}".format(stop-start))