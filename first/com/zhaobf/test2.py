# 斐波纳契数列

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

print("=================================")

a, b = 0, 1
while b < 1000:
    print(b,end=" ")
    a, b = b, a + b
