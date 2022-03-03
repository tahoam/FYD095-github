# Txt from canvas page. In the same folder as the assignment2.py
filename = './name_list.txt'
names = {}
with open(filename) as data:
    for line in data:
        name = line.rstrip()
        print(name)
        if name in names:
            names[name] = names.get(name) + 1
        else:
            names[name] = 1
print(names)