import copy

with open('input_5.txt') as file:
    text = file.readlines()
    lists = list(zip(*text[:9]))
    for i, row in enumerate(lists):
        lists[i] = [n for n in row if n.isalpha()]
    stacks = [el for el in lists if el]

result1 = copy.deepcopy(stacks)
for row in text[10:]:
    r = row.split()
    y, z = int(r[3])-1, int(r[5])-1
    for _ in range(int(r[1])): # move x from y to z
        result1[z].insert(0, result1[y][0])
        result1[y] = result1[y][1:]

result1 = [el[0] for el in result1]
print('first star: ', *result1, sep = '')

result2 = copy.deepcopy(stacks)

for row in text[10:]:
    r = row.split()
    x = int(r[1]) # move x from y to z
    y, z = int(r[3])-1, int(r[5])-1
    result2[z] = result2[y][:x] + result2[z]
    result2[y] = result2[y][x:]

result2 = [el[0] for el in result2]
print('second star: ', *result2, sep = '')
