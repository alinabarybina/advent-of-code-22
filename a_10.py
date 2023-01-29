# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.

cycle = 1
X = [0,1]
lst = [20, 60, 100, 140, 180, 220]
result = 0

with open('input_10.txt') as file:
    while cycle < 220:
        match file.readline().split():
            case ['noop']:
                cycle += 1
            case ['addx', s]:
                cycle += 2
                X[0], X[1] = X[1], X[1] + int(s)
        if cycle == lst[0]:
            result += X[1] * lst[0]
            lst.pop(0)
        elif lst[0] < cycle < lst[0] + 2:
            result += X[0] * lst[0]
            lst.pop(0)

print('first star:', result)

# What eight capital letters appear on your CRT?

result2 = [['.' for _ in range(40)] for _ in range(6)]

with open('input_10.txt') as file:
    cycle = 0
    X = 1
    while cycle < 40 * 6:
        signal = file.readline().split()
        match signal:
            case ['noop']:
                if X - 1 <= cycle%40 <= X + 1:
                    result2[cycle//40][cycle%40] = '#'
                cycle += 1
                
            case ['addx', s]:
                if X - 1 <= cycle%40 <= X + 1:
                    result2[cycle//40][cycle%40] = '#'
                if X - 1 <= (cycle+1)%40 <= X + 1:
                    result2[(cycle+1)//40][(cycle+1)%40] = '#'
                cycle += 2
                X += int(s)

for row in result2:
    print(*row) # RKPJBPLA