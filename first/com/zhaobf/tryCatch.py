# Python3 错误和异常
# import sys
#
# try:
#     i = int(input("请输入一个整数"))
# except:
#     print(sys.exc_info())
#     raise
# else:
#     print(i)




# try:
#     raise NameError("HiHere")
# except NameError:
#     print("An exception flew by ")
#     raise




# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
#
# try:
#     raise MyError(2 * 2)
# except MyError as e:
#     print("My exception occurred, value:", e.value)
#
#
# class BaseError(Exception):
#     pass
#
#
# class TransitionError(BaseError):
#     def __init__(self, message):
#         self.message = message




# try:
#     raise KeyboardInterrupt
# finally:
#     print("Goodbye, world")




def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)
print(">>>>>>>>>>>")
divide(2, 0)
print(">>>>>>>>>>>")
divide("2","1")