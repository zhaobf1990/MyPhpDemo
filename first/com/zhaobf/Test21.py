def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        print(people)
        if people:
            people.append(full_name)
        else:
            data[label][name] = full_name
            print(data[label][name])


myname = {}
init(myname)
store(myname, 'wu jiao jiao')