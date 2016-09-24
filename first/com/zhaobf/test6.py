# Python3 函数

# def add(a, b):
#     return a + b
#
#
# def aera(a, b):
#     return a * b
#
#
# print(add(1, 2))
#
# print(add("1", "3"))
#
# print( aera("a",8))


# 标题:按值传递参数和按引用传递参数
# 在 Python 中，所有参数（变量）都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
def changeme(data):
    "修改传入的列表"
    data.append([1, 2, 3, 4]);
    print("函数内取值: ", data)
    return data


# 调用changeme函数
mylist = [10, 20, 30];
c = changeme(mylist);
print (c)
print ("函数外取值: ", mylist)


# # 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出arg1: ", arg1)
#
#     for var in vartuple:
#         print("vartuple", var)
#     return;
#
#
# # 调用printinfo 函数
# # printinfo(10);
# printinfo(70, 60, 50);




# sum1=lambda arg1,arg2:arg1+arg2;
#
# print("相加后的值为:",sum1(10,20))
# sum()

def add(a):
    a = 2
    return a


b = 1
c = add(b)
print(c)
print(b)
