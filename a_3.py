d = {chr(i): i-96 for i in range(97, 123)}
d.update({chr(i): i-38 for i in range(65, 91)})

result = 0

with open('input_3.txt', encoding = 'utf-8') as file:
    for row in file.readlines():
        r = row.strip()
        r1 = set(r[:int(len(r)/2)])
        r2 = set(r[int(len(r)/2):])
        common = ''.join(r1 & r2)
        result += d[common]

print('first star:', result)

# part 2
result2 = 0

with open('input_3.txt', encoding = 'utf-8') as file:
    text = file.readlines()
           
for i in range(0,len(text),3):
    r1 = set(text[i].strip())
    r2 = set(text[i+1].strip())
    r3 = set(text[i+2].strip())           
    
    common = ''.join(r1 & r2 & r3)
    result2 += d[common]

print('second star:', result2)