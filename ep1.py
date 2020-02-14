def make_class(x):
    class New:
        def __init__(self, name):
            self.name = name
        def print_x():
            print(x)
    return New

var = make_class(10)
inst = var("Jim")
var.print_x()
print(inst.name)


for i in range(10):
    def show():
        print(i*2)
    show()
show()



def func(x):
    if(x==1):
        def ret_val():
            print("X is 1")
    else:
        def ret_val():
            print("X is", x)
    return ret_val
fun_inst = func(5)
print(id(fun_inst))
fun_inst()



import inspect
print(inspect.getsource(fun_inst))


from queue import Queue
print(inspect.getsource(Queue))
