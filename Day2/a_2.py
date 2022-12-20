# [0] - opponent: A for Rock, B for Paper, and C for Scissors
# [1] - you: X for Rock, Y for Paper, and Z for Scissors
# + score - 1 for Rock, 2 for Paper, and 3 for Scissors

opponent = ['A', 'B', 'C']
you = ['X', 'Y', 'Z']

opponent_score = 0
your_score = 0

result = ['draw', 'opponent', 'you']

with open('input_2.txt') as file:
    for row in file:
        r = row.split()
        opponent_score += opponent.index(r[0]) + 1
        your_score += you.index(r[1]) + 1
        n = opponent.index(r[0]) - you.index(r[1])
        if result[n] == 'draw':
            opponent_score += 3
            your_score += 3
        elif result[n] == 'opponent':
            opponent_score += 6
        elif result[n] == 'you':
            your_score += 6

print('first star:', your_score)

# second star
# [0] - opponent: A for Rock, B for Paper, and C for Scissors
# Y means you need to end the round in a draw, X means you need to lose, and Z means you need to win
# + score - 1 for Rock, 2 for Paper, and 3 for Scissors

opponent = ['A', 'B', 'C']
guide = ['Y', 'X', 'Z']

opponent_score = 0
your_score = 0

with open('input_2.txt') as file:
    for row in file:
        r = row.split()
        opponent_score += opponent.index(r[0]) + 1
        # you_score += opponent.index(r[0]) - you.index(r[1]) + 1
        if r[1] == 'Y':
            opponent_score += 3
            your_score += 3
            your_score += opponent.index(r[0]) + 1
        elif r[1] == 'X':
            opponent_score += 6
            your_score += opponent.index(opponent[opponent.index(r[0])-1]) + 1
        elif r[1] == 'Z':
            your_score += 6
            your_score += opponent.index(opponent[opponent.index(r[0])+(1 if opponent.index(r[0]) < 2 else -2)]) + 1

print('second star:', your_score)
