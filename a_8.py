trees = []

with open('input_8.txt') as file:
    for row in file:
        trees.append([[int(n), True] for n in row.strip()])

y_left = 0
y_right = 0

for i, row in enumerate(trees):
    shortest = row[0][0]
    y_left += row[0][1]
    trees[i][0] = False
    for j, n in enumerate(row[1:],1):
        if n[0] > shortest:
            shortest = n[0]
            y_left += n[1]
            trees[i][j][1] = False

    shortest = row[-1][0]
    y_right += row[-1][1]
    trees[i][-1][1] = False
    for j in range(len(row)-1,0,-1):
        if trees[i][j][0] > shortest:
            shortest = trees[i][j][0]
            y_right += trees[i][j][1]
            trees[i][j][1] = False

print('y_left:', y_left)
print('y_right:', y_right)

x_upper = 0
x_down = 0

for i in range(1, len(trees[0])):
    shortest = trees[0][i][0]
    x_upper += trees[0][i][1]
    trees[0][i][1] = False
    for j in range(1, len(trees)):
        if trees[j][i][0] > shortest:
            shortest = trees[j][i][0]
            x_upper += trees[j][i][1]
            trees[j][i][1] = False

    shortest = trees[-1][i][0]
    x_down += trees[-1][i][1]
    trees[0][i][1] = False
    for j in range(len(trees)-1, 0, -1):
        if trees[j][i][0] > shortest:
            shortest = trees[j][i][0]
            x_upper += trees[j][i][1]
            trees[j][i][1] = False

print('x_upper:', x_upper)
print('x_down:', x_down)

print('first star:', y_left + y_right + x_upper + x_down)

# 2. star
with open('input_8.txt') as file:
    trees = [[int(n) for n in row.strip()] for row in file.readlines()]

max_score = 0
for i, row in enumerate(trees[1:len(trees)-1], 1):
    for j, tree in enumerate(row[1:len(row)-1], 1):
        score = 1
        #rows down
        count_a = 0
        for a in range(i+1,len(trees)):
            if trees[a][j] < tree:
                count_a += 1
            elif trees[a][j] >= tree or a == len(trees):
                count_a += 1
                break
        #rows up
        count_b = 0
        for b in range(i-1,-1,-1):
            if trees[b][j] < tree:
                count_b += 1
            elif trees[b][j] >= tree or b == 0:
                count_b += 1
                break
        #cols right
        count_c = 0
        for c in range(j+1,len(row)):
            if trees[i][c] < tree:
                count_c += 1
            elif trees[i][c] >= tree or c == len(row):
                count_c += 1
                break
        #cols left
        count_d = 0
        for d in range(j-1,-1,-1):
            if trees[i][d] < tree:
                count_d += 1
            elif trees[i][d] >= tree or d == 0:
                count_d += 1
                break
        score = count_a * count_b * count_c * count_d
        if score > max_score:
            max_score = score
    
print('second star:', max_score)