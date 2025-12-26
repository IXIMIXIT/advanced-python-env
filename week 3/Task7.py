import math

# 7.1: Quad area with one right angle
def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Task 7.1: Special Quad Area")
x, y, z, t = float(input()), float(input()), float(input()), float(input())
area1 = 0.5 * x * y
diag = math.sqrt(x**2 + y**2)
area2 = heron(z, t, diag)
print(area1 + area2)

# 7.2: Integer to 10-digit Octal
print("\nTask 7.2: Octal Converter")
n = int(input())
o = oct(n)[2:]
print(o.zfill(10))
