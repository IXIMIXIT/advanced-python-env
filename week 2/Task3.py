eq = input().strip()
a, op, b, _, c = eq[0], eq[1], eq[2], eq[3], eq[4]

if a == 'x':
    if op == '+':
        print(int(c) - int(b))
    else:
        print(int(c) + int(b))
elif b == 'x':
    if op == '+':
        print(int(c) - int(a))
    else:
        print(int(a) - int(c))
else:
    if op == '+':
        print(int(a) + int(b))
    else:
        print(int(a) - int(b))
