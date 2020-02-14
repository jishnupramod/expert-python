class Test:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Person is {self.name}"
    def __mul__(self, num):
        if(type(num) is not int):
            raise Exception("Invalid argument, integer expected")
        self.name = self.name * num
    def __call__(self, arg):
        print("Called function:", arg)
    def __len__(self):
        return len(self.name)

t = Test("user")
t * 3
t(4)
print(t)
print(len(t))


from queue import Queue as q
import inspect

# print(inspect.getsource(q))

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"
    def __add__(self, x):
        self._put(x)
    def __sub__(self, x):
        self._get()
que = Queue()
print(que)
que + 1
print(que)
que + 2
print(que)
que - 3
print(que)
