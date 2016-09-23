def store(data, full_name):
    names = full_name.split()  # 3
    if len(names) == 2: names.insert(1, '')  # 4
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):  # 5
        people = lookup(data, label, name)
        if people:
            people.append(full_name)  # 6
        else:
            data[label][name] = [full_name]
