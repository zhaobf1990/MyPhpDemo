# Python3 循环语句

a = 1;

while a <= 10:
    print(a, end=", ")
    a += 1
else:
    print("大于10的数据不输入 ")

print("===============================")

list = [1, 2, 3, 4, 5, 6, 7, 8]

for item in list:
    print(item, end=", ")
else:
    print("结束")

print("===============================")

for item in list:
    if item == 3:
        break
    else:
        print(item, end=", ")
else:
    print("结束")

print("")
print("===============================")
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
list3 = range(6)
for i in list3:
    print(i, end=", ")

print("")
print("===============================")
# 你也可以使用range指定区间的值：
list4 = range(4, 7)
for i in list4:
    print(i, end=", ")

print("")
print("===============================")
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
list5 = range(4, 20, 3)
for i in list5:
    print(i, end=", ")

print("")
print("===============================")
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i],end=", ")

print("")
print("===============================")
while True:
    pass



