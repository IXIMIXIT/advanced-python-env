import math

# 7.1: Quad area with one right angle
def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

print("--- Task 7.1: Special Quad Area ---")
X, Y, Z, T = float(input("X: ")), float(input("Y: ")), float(input("Z: ")), float(input("T: "))
area1 = 0.5 * X * Y
diag = math.sqrt(X**2 + Y**2)
area2 = heron(Z, T, diag)
print(f"Total Area: {area1 + area2:.2f}")

# 7.2: Integer to 10-digit Octal
print("\n--- Task 7.2: Octal Converter ---")
n = int(input("Enter non-negative int: "))
print(f"{oct(n)[2:].zfill(10)}")