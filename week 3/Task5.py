def gcd(a, b):
    while b: a, b = b, a % b
    return a

# 5.1: Subtract fractions (A/B) - (C/D)
print("Task 5.1: Subtract Fractions")
A, B, C, D = int(input("A: ")), int(input("B: ")), int(input("C: ")), int(input("D: "))
num, den = (A * D) - (C * B), B * D
common = gcd(abs(num), den)
print(f"Result: {num//common}/{den//common}")


