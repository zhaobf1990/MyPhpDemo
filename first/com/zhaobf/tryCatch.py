# Python3 错误和异常
import sys

try:
    i = int(input("请输入一个整数"))
except:
    print(sys.exc_info())
    raise
else:
    print(i)
