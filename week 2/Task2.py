def is_cyclic_shift(sub, b):
    if len(sub) != len(b): return False
    return sub in (b + b) and len(sub) == len(b)

a = input().strip()
b = input().strip()
count = 0
m = len(b)

for i in range(len(a) - m + 1):
    substring = a[i:i+m]
    if is_cyclic_shift(substring, b):
        count += 1
print(count)