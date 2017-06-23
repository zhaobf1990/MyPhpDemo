import os
caselist = os.listdir(r"F:\360PhoneInfo")
print(caselist)
for a in caselist:

    s = a.split('.')[1]
    # print(s)
    if s == 'py':
        print(r'F:\360PhoneInfo\%s >>log.txt 2>&1' % a);
        os.system(r'F:\360PhoneInfo\%s >>log.txt 2>&1' % a);

# # os.system('C:\\Users\\Administrator\\PycharmProjects\\PythonTest001\\wjj\\test_case\\%s 1>>log.txt 2>&1' % a)
