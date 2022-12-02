total_score = 0
guide = {
    'A':{'X':(1+3), 'Y':(2+6), 'Z':(3+0)},
    'B':{'X':(1+0), 'Y':(2+3), 'Z':(3+6)},
    'C':{'X':(1+6), 'Y':(2+0), 'Z':(3+3)}
}

with open('input.txt', 'r') as f:
    for line in f:
        m1 = line[0]
        m2 = line[2]
        total_score += guide[m1][m2]

print(total_score)