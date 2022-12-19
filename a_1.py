with open('input_1.txt', encoding = 'utf-8') as file:
    text = file.readlines()

res = []
counter = 0

for i, row in enumerate(text):
    r = row.strip()
    if i == len(text) - 1:
        counter += int(r)
        res.append(counter)
    elif r:
        counter += int(r)
    elif r == '':
        res.append(counter)
        counter = 0

print('first star:', max(res))
print('second star:', sum(sorted(res, reverse = True)[:3]))