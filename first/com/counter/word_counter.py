# coding=utf-8

import collections
import os
import re

with open('article') as file1:  ##  打开文本文件
    str = file1.read().replace("\n", " ")
    str1 = re.split(' |,|/|-|\.|\)|\(|=|_|<|>|#|\?|\\t', str)  # 将文章按照空格划分开

# print "原文本:\n %s" % str1

# print "\n各单词出现的次数：\n %s" % collections.Counter(str1)
# print collections.Counter(str1)['was']#以字典的形式存储，每个字符对应的键值就是在文本中出现的次数

counter = collections.Counter(str1)

dirs = counter.items()

# sorted(dirs, key=dirs(1), reverse=True)

# print  dirs

result = sorted(dirs, key=lambda item: item[1])

result.reverse()
# print  result
for a in result:
    print  a
