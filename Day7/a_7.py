dirs = {}

with open('input_7.txt') as file:
    text = file.readlines()

name = '/'
for i, row in enumerate(text):
    r = row.split()
    if r == ['$', 'cd', '/']:
        size = 0
        inside_dirs = []
        for j in range(i+2, len(text)): 
            l = text[j].split()
            if l[0].isdigit():
                size += int(l[0])
            elif l[0] == 'dir':
                inside_dir_name = name + ' ' + l[1]
                inside_dirs.append(inside_dir_name)
            elif l[0] == '$':
                break
            dirs.update({name : [size] + inside_dirs})
    elif r == ['$', 'cd', '..']:
        name = ' '.join(name.split()[:-1])
    elif r[:2] == ['$', 'cd']:
        name = name + ' ' + r[2]
        if r[0:2] == ['$', 'cd'] and '$ ls' in text[i+1] and r[2] not in dirs:
            size = 0
            inside_dirs = []
            for j in range(i+2, len(text)): 
                l = text[j].split()
                if l[0].isdigit():
                    size += int(l[0])
                elif l[0] == 'dir':
                    inside_dir_name = name + ' ' + l[1]
                    inside_dirs.append(inside_dir_name)
                elif l[0] == '$':
                    break
            dirs.update({name : [size] + inside_dirs})

dirs_sorted = {k: v for k, v in sorted(dirs.items(), key = lambda item: len(item[1]))}

step = 0
while step < 20:
    for item1 in dirs.items():
        if isinstance(dirs[item1[0]], int) or (isinstance(dirs[item1[0]],list) and len(item1[1]) == 1):
            for item2 in dirs.items():
                if isinstance(item2[1], list) and item1[0] in item2[1]:
                    i = item2[1].index(item1[0])
                    vals = item2[1]
                    vals[i] = item1[1][0] if isinstance(dirs[item1[0]],list) else item1[1]
                    dirs[item2[0]] = vals

        elif isinstance(dirs[item1[0]], list) and all(map(lambda x: isinstance(x, int), dirs[item1[0]])):
            dirs[item1[0]] = sum(item1[1])

    step += 1

print()
for i in dirs.items():
    dirs[i[0]] = i[1] if isinstance(i[1], int) else sum(i[1])

res = 0

for item in dirs.items():
    if item[1] <= 100000:
        res += item[1]
        print(item)

print('first star:', res)

print(dirs['/'])
total_size = 70000000
print('free_space', free_space := total_size - dirs['/'])
print('space_needed', space_needed := 30000000)
print('space_to_free', space_to_free := space_needed - free_space)

dirs_filtered = {}

for i in dirs.items():
    if i[1] >= space_to_free:
        dirs_filtered.update({i[0]: i[1]})

print('second star:', min(dirs_filtered.values()))
