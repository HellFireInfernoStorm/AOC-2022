def compare(l1, l2):
    if l1 == l2:
        return None
    if not bool(l1):
        return True
    if not bool(l2):
        return False
    l1 = l1[1:] if l1[0] == ',' else l1
    l2 = l2[1:] if l2[0] == ',' else l2
    a, l1 = l1[0], l1[1:]
    b, l2 = l2[0], l2[1:]

    if a.isdigit() and b.isdigit():
        while bool(l1):
            if not l1[0].isdigit():
                break
            a, l1 = a+l1[0], l1[1:]
        while bool(l2):
            if not l2[0].isdigit():
                break
            b, l2 = b+l2[0], l2[1:]
        a, b = int(a), int(b)
        if a < b:
            return True
        if a > b:
            return False
        return compare(l1, l2)

    if a == '[':
        c = 1
        while bool(l1):
            nextChar, l1 = l1[0], l1[1:]
            a += nextChar
            if nextChar == '[':
                c += 1
                continue
            if nextChar == ']':
                c -= 1
            if c == 0:
                break
        a = a[1:-1]
    else:
        while bool(l1):
            if not l1[0].isdigit():
                break
            a, l1 = a+l1[0], l1[1:]

    if b == '[':
        c = 1
        while bool(l2):
            nextChar, l2 = l2[0], l2[1:]
            b += nextChar
            if nextChar == '[':
                c += 1
                continue
            if nextChar == ']':
                c -= 1
            if c == 0:
                break
        b = b[1:-1]
    else:
        while bool(l2):
            if not l2[0].isdigit():
                break
            b, l2 = b+l2[0], l2[1:]

    result = compare(a, b)
    if result != None:
        return result
    return compare(l1, l2)


with open('input.txt') as f:
    data = [[line[1:-1] for line in lines.splitlines()] for lines in f.read().split('\n\n')]

total = 0
for i in range(len(data)):
    if compare(*data[i]):
        total += i + 1

print(total)