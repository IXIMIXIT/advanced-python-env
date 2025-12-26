def gcd(a, b):
    while b: a, b = b, a % b
    return a

# 4.1: Divide fractions (A/B) / (C/D)
print("Task 4.1: Divide Fractions")
num = int(input()) * int(input())
den = int(input()) * int(input())
common = gcd(num, den)
print(f"{num // common}/{den // common}")


# 4.2: Points inside a circle
def is_in(px, py, r):
    return (px**2 + py**2) <= r**2

r_val = float(input())
pts = [(1, 2), (5, 5), (0, 1)]
count = 0
for x, y in pts:
    if is_in(x, y, r_val):
        count += 1
print(count)
