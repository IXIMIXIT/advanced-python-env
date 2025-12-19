eq = input().strip()
a, op, b, _, c = eq[0], eq[1], eq[2], eq[3], eq[4]

if a == 'x':
    res = int(c) - int(b) if op == '+' else int(c) + int(b)
elif b == 'x':
    res = int(c) - int(a) if op == '+' else int(a) - int(c)
else: # c == 'x'
    res = int(a) + int(b) if op == '+' else int(a) - int(b)
print(res)