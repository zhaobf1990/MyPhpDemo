#coding=utf-8
import csv
My_file="D:/GitHubWorkSpace/MyPhpDemo/first/wjj/userinfo1.csv"
# data=csv.reader(open(My_file,'r'))
with open(My_file,'r',) as csvfile:
    data=csv.reader(csvfile)
    for user in data:
        print(user[0])
        print(user[1])
        print(user[2])
        print(user[3])
