def gcd(a, b):
    while b: a, b = b, a % b
    return a

# 4.1: Divide fractions (A/B) / (C/D)
print("--- Task 4.1: Divide Fractions ---")
A, B, C, D = int(input("A: ")), int(input("B: ")), int(input("C: ")), int(input("D: "))
num, den = A * D, B * C
common = gcd(num, den)
print(f"Irreducible Fraction: {num//common}/{den//common}")

# 4.2: Points inside a circle
def is_inside(px, py, R):
    return (px**2 + py**2) <= R**2

print("\n--- Task 4.2: Points in Circle ---")
R = float(input("Radius: "))
points = [("P", float(input("P1: ")), float(input("P2: "))), 
          ("F", float(input("F1: ")), float(input("F2: "))), 
          ("L", float(input("L1: ")), float(input("L2: ")))]
count = sum(1 for name, x, y in points if is_inside(x, y, R))
print(f"Points inside: {count}")