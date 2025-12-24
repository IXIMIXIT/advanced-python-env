import math

def gcd(a, b):
    while b: a, b = b, a % b
    return a

# 6.1: GCD and LCM
print("--- Task 6.1: GCD and LCM ---")
a, b = int(input("A: ")), int(input("B: "))
g = gcd(a, b)
print(f"GCD: {g}, LCM: {(a * b) // g}")

# 6.2: Convex Quad Area (4 sides + 1 diagonal)
def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

print("\n--- Task 6.2: Quad Area ---")
s1, s2, s3, s4, diag = [float(input(f"Value {i+1}: ")) for i in range(5)]
print(f"Area: {heron(s1, s2, diag) + heron(s3, s4, diag):.2f}")