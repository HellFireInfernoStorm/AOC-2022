from math import prod

with open('input.txt') as f:
    monkeys = [monkey.split('\n') for monkey in f.read().split('\n\n')]

n = len(monkeys)
items = dict()
operations = dict()
tests = dict()
inspectionCount = dict()


for monkey in monkeys:
    index = int(monkey[0][-2])
    items[index] = list(map(int, monkey[1][18:].split(', ')))
    operator = monkey[2][23]
    operand = monkey[2][25:]
    operations[index] = [operator, operand]
    test = int(monkey[3][21:])
    trueMonkey = int(monkey[4][-1])
    falseMonkey = int(monkey[5][-1])
    tests[index] = [test, trueMonkey, falseMonkey]
    inspectionCount[index] = 0

moduloVal = prod([tests[i][0] for i in range(n)])

def inspect(item, operation):
    operand = int(operation[1]) if (operation[1] != 'old') else item
    match operation[0]:
        case '*':
            return item * operand
        case '+':
            return item + operand

def test(item, testVal):
    if item % testVal == 0:
        return True
    return False

def execRound():
    for i in range(n):
        for item in items[i]:
            item = inspect(item, operations[i]) % moduloVal
            inspectionCount[i] += 1
            if test(item, tests[i][0]):
                items[tests[i][1]].append(item)
            else:
                items[tests[i][2]].append(item)
        items[i] = []

round_count = 10000
for _ in range(round_count):
    execRound()

totals = list(inspectionCount.values())
totals.sort(reverse=True)
monkeyBusiness = totals[0] * totals[1]

print(monkeyBusiness)