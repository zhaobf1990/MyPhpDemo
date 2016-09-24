# s = "Hello,Ru\nnoob"
# print(str(s))
# print(repr(s))
# print(1 / 7)
# print(str(1 / 7))
# print(repr(1 / 7))
# a = 12
# print(str(a))
#
# x = 10 * 3.25
# y = 200 * 200
# s1 = "x的值为:" + repr(x) + ", y的值为:" + repr(y) + ", s的值为:" + repr(s)
# print(s1)
# print("x的值为:" + str(x) + ", y的值为:" + str(y) + ", s的值为:" + str(s))
# print((x, y, ('Google', 'Runoob')))
# print(repr((x, y, ('Google', 'Runoob'))))
#
# for x in range(1, 11):
#     print(repr(x).rjust(4), repr(x * x).rjust(4), end=" ")
#     print(repr(x * x * x).rjust(4))
#
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x ** 2, x ** 3))
#
# print("{0:10} ========= {1:10}".format("sdf", "sfsfsf"))
#
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print("Runoob:{0[Runoob]}; Google:{0[Google]}; Taobao:{0[Taobao]}".format(table))
#
# import math
#
# print("常量PI的值近似为: %5.3f." % math.pi)
#
# str = input("请输入:")
# print("你输入的是:", str)

# file = open("hello.txt", "a")
# print(type(file))
# file.write("python 是一个非常好的语言")
# file.close()
#
# file = open("hello.txt")
# # str = file.readline()
# for line in file:
#     print(line)
# # print(str)


# value=("www.baidu.com",1)
# s=str(value)
# file=open("hello.txt","w")
# file.write(s);
# print(file.tell())
# file.close()


# with open("hello.txt") as f:
#     print(f.readline())
# f.close()

# import pickle
# list=["ad","sfw"]
# file=open("hello.txt","w")
# pickle.dump(list,file)
# file.close()

import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output=open("hello.txt","wb")
pickle.dump(data1,output)

pickle.dump(selfref_list, output, -1)
output.close()

import pprint
pkl_file = open('hello.txt', 'rb')
data1=pickle.load(pkl_file)
pprint.pprint(data1);
data2=pickle.load(pkl_file)
pprint.pprint(data2)

