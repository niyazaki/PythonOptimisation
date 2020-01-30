from guppy import hpy

h = hpy()
list1 = []
for i in range(1000):
     list1.append(str(i))
print(h.heap().size)

h = hpy()
list1 = range(1000)
print(h.heap().size)

