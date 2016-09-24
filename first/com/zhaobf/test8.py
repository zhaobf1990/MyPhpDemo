# vec = [2, 4, 6]
# list=[3 * x for x in vec]
# print(list)



# list = ["1111", "2222", "3333", "4444"]
# list3 = [[x,list[x]] for x in range(4)]
# print (list3)



# list = ["1111", "2222", "3333", "4444"]
# list3 = [[x, list[x]] for x in range(4) if x % 2 == 0]
# print (list3)



# list1=[2,4,6]
# list2=[4,8,12]
# list3=[x*y for x in list1 for y in list2 ]
# print (list3)




# print([str(round(355 / 113, i)) for i in range(1, 6)])



#
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print [row[1] for row in matrix]
# list=[row[1] for row in matrix]
# print (list)
# list=[[row[i] for row in matrix] for i in range(4)]
# print(list)
# list=[]
# for i in range(4):
#     list.append([row[i] for row in matrix])
# print (list)
def story(**kwds):
    return 'once upon a time.there was a %(job)s called %(name)s' % kwds


def power(x, y, *other):
    if other:
        print('receivede redundant:', other)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'imitates range() for step>0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


# print(story(job='king', name='gumi'))
# params={'job':'language','name':'python'}
# print(story(**params))
# del params['job']
# print(story(job='ok',**params))
# print(power(3,2))
# print(power(y=3,x=2))
# params=[5,]*2
# print(params)
# print(power(*params))
# print(power(3,3,'params'))
# print(interval(10))
print(interval(3, 7))
# print(interval(3,12,4))
print(power(*interval(3, 7)))
