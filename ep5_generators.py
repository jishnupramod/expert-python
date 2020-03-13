# class Generator:
#     def __init__(self, n):
#         self.n = n
#         self.last = 0
#
#     def __next__(self):
#         return self.next()
#
#     def next(self):
#         if(self.last == self.n):
#             raise StopIteration()
#
#         rv = self.last ** 2
#         self.last += 1
#         return rv
#
# gen = Generator(100)
#
# while(True):
#     try:
#         print(next(gen))
#     except StopIteration:
#         break

import sys

def generator(n):
    for i in range(n):
        yield i**2

g = generator(10000)
x = [i**2 for i in range(10000)]

print("Size of list:", sys.getsizeof(x))
print("Size of generator:", sys.getsizeof(g))
