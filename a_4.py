with open('input_4.txt') as file:
    text = file.readlines()

result1 = 0

for row in text:
    r = row.strip().split(',')
    r1 = list(map(int, r[0].split('-')))
    r2 = list(map(int, r[1].split('-')))
    set1 = set(range(r1[0], r1[1]+1))
    set2 = set(range(r2[0], r2[1]+1))
    if (set1.issubset(set2)) or (set2.issubset(set1)):
        result1 += 1

print('first star:', result1)

# part 2

result2 = 0

for row in text:
    r = row.strip().split(',')
    r1 = list(map(int, r[0].split('-')))
    r2 = list(map(int, r[1].split('-')))

    set1 = set(range(r1[0], r1[1]+1))
    set2 = set(range(r2[0], r2[1]+1))

    if set1 & set2:
        result2 += 1

print('second star:', result2)