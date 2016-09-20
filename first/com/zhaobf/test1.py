# 去空格及特殊符号
s = "    abc,   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.rstrip())

name = 'python'
name = 'zhaobf'
print(name)

print("zhao\nswfw")
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
print(r"zhao\nswfw")

# List（列表）
print("================")
list = ["abcd", 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'sss']

print(list)
print(list[0])
print(list * 2)
print(list + tinylist)
list = []
print(list)

# Tuple（元组）
tup = ()
print(tup)
tup = ("sfww")
print(type(tup))
tup = ("sfww",)
print(type(tup))

# set(集合)
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号({})或者 set()函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
student = {"Tom", "Jim", "Mary", "Tom", "Jack", "Rose"}
print(student)

if ("Rose" in student):
    {
        print("Rose在集合中")
    }
else:
    {
        print("Rose不在集合中")
    }

# set可以进行集合运算
a = set("abracadabra")
b = set("alacazam")

print(type(a))
print(a)
print(a - b)


# Dictionary（字典）（字典）
dic={}
dic["one"]="1 - 菜鸟教程"
dic[2]="2 - 菜鸟工具"
tinyDic={"name":"runoob","code":1,"site":"www.baidu.com"}

print(dic["one"])
print(  dic[2])
print(dic)
print(dic.keys())
print(dic.values())

a=dict([("runoob",1),("google,2"),("taobao",3)])
print(a)


{x:x**2 for x in (2.4,6)}

# dict=