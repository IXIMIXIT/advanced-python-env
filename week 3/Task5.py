def gcd(a, b):
    while b: a, b = b, a % b
    return a

# 5.1: Subtract fractions (A/B) - (C/D)
print("--- Task 5.1: Subtract Fractions ---")
A, B, C, D = int(input("A: ")), int(input("B: ")), int(input("C: ")), int(input("D: "))
num, den = (A * D) - (C * B), B * D
common = gcd(abs(num), den)
print(f"Result: {num//common}/{den//common}")

# 5.2: All divisors of a number
print("\n--- Task 5.2: Divisors ---")
n = int(input("Number: "))
print(*(i for i in range(1, n + 1) if n % i == 0))