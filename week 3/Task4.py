def gcd(a, b):
    while b: a, b = b, a % b
    return a

# 4.1: Divide fractions (A/B) / (C/D)
print("Task 4.1: Divide Fractions")
num = int(input()) * int(input())
den = int(input()) * int(input())
common = gcd(num, den)
print(f"{num // common}/{den // common}")



