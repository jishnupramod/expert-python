# class Test:
#     pass
Test = type('Test', (), {})   # Equivalent to above class definition
print(Test)
print(Test())

Test2 = type('Test2', (), {"x": 50})
t = Test2()
t.wel = "Hello, meta"
print(t.x, t.wel)

# inheritance
class Foo:
    def disp(self):
        print("Displaying...")
Test3 = type('Test3', (Foo,), {})
t3 = Test3()
t3.disp()

# Using function
def add_attr(self):
    self.var = 10
Test4 = type('Test4', (), {"add_attr": add_attr})
t4 = Test4()
t4.add_attr()
print(t4.var)

# Metaclasses
class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        dic = {}
        for name, val in attrs.items():
            if(name.startswith("__")):
                dic[name] = val
            else:
                dic[name.upper()] = val
        print(dic)
        # return type(class_name, bases, attrs)
        return type(class_name, bases, dic)

class Test5(metaclass=Meta):
    var1 = 6
    var2 = "Hello"
    def func(self):
        print("Fun")

t5 = Test5()
# print(t5.var1) # Error
print(t5.VAR1) # outputs 6
# t5.func() # Error
t5.FUNC() # Calls
