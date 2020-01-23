# Source : https://www.geeksforgeeks.org/optimization-tips-python-code/?fbclid=IwAR0csqvCRMSA5_Rn-r7RDcnx_PXRHLXgUfhn-tQidlLNQyZmqva4cDZZafY

import timeit
from guppy import hpy

# slower
start = timeit.default_timer()
h = hpy()

x = 2
y = 5
temp = x
x = y
y = temp

stop = timeit.default_timer()
print("Time from start : {}".format(stop-start))
print("memory consumption : {}".format((h.heap()).size))

# faster
start = timeit.default_timer()
h = hpy()

x, y = 3, 5
x, y = y, x


stop = timeit.default_timer()
print("Time from start : {}".format(stop-start))
print("memory consumption : {}".format((h.heap()).size))
