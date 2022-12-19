with open('input_6.txt') as file:
    text = file.read()

for i in range(len(text)):
    if len(set(text[i:i+4])) == 4:
        print('first star:', i+4)
        break

for i in range(len(text)):
    if len(set(text[i:i+14])) == 14:
        print('second star', i+14)
        break