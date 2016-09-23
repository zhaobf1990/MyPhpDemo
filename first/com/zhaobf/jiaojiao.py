def init(data):  # 1
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


MyNames = {}
init(MyNames)
print(MyNames)





























# def lookup(data, label, name):
#     return data[label].get(name)  # 2
#
#
# def store(data, full_name):
#     names = full_name.split()  # 3
#     print("names=", names)
#     if len(names) == 2: names.insert(1, '')  # 4
#     labels = 'first', 'middle', 'last'
#     for label, name in zip(labels, names):  # 5
#         people = lookup(data, label, name)
#     if people:
#         people.append(full_name)  # 6
#     else:
#         data[label][name] = [full_name]


# MyNames = {}
# init(MyNames)
# store(MyNames, 'Magnus Lie Hetland')
# print(lookup(MyNames, 'middle', 'Lie'))
