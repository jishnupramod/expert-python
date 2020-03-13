###################   Training Phase    #####################

    # def func(string):
    #     def wrapper():
    #         print("Started")
    #         print(string)
    #         print("Ended")
    #     return wrapper
    #
    # # x = func("hello")
    # # print(x)
    # # x()
    #
    # def funct(f):
    #     def wrapper(*args, **kwargs):
    #         print("Started")
    #         rv = f(*args, **kwargs)
    #         print("Ended")
    #         print()
    #         return rv
    #     return wrapper
    #
    # @funct
    # def func2():
    #     print("This is func2")
    #
    # # x = funct(func2)
    # # print(x)
    # # x()
    #
    # func2()
    #
    # @funct
    # def func3(x):
    #     print(x)
    # func3(10)
    #
    # @funct
    # def func4(x, y):
    #     print(x)
    #     return y
    # z = func4(100, 200)
    # print(z)


######################   Test Phase   ####################
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Total running time:", total)
        return rv
    return wrapper


# def test():
#     @timer
#     def fact(n):
#         if n == 1:
#             return 1
#         else:
#             return n*fact(n-1)
#     return fact
#
# f = test()
# print(f(5))

@timer
def test():
    for i in range(10000000):
        pass
test()

@timer
def test2():
    time.sleep(3)

test2()
