total_score = 0
guide = {
    'A':{'X':(3+0), 'Y':(1+3), 'Z':(2+6)},
    'B':{'X':(1+0), 'Y':(2+3), 'Z':(3+6)},
    'C':{'X':(2+0), 'Y':(3+3), 'Z':(1+6)}
}

with open('input.txt', 'r') as f:
    for line in f:
        m1 = line[0]
        m2 = line[2]
        total_score += guide[m1][m2]

print(total_score)