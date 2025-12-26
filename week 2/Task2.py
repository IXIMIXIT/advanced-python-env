a = input().strip()
b = input().strip()
count = 0
m = len(b)
doubled_b = b + b

for i in range(len(a) - m + 1):
    sub = a[i:i+m]
    if sub in doubled_b and len(sub) == len(b):
        count += 1

print(count)
