import math

def gcd(a, b):
    while b: a, b = b, a % b
    return a

# 6.1: GCD and LCM
print("Task 6.1: GCD and LCM")
a, b = int(input()), int(input())
g = gcd(a, b)
lcm = (a * b) // g
print(g, lcm)

# 6.2: Convex Quad Area (4 sides + 1 diagonal)
print("\nTask 6.2: Quad Area")
def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

s1 = float(input())
s2 = float(input())
s3 = float(input())
s4 = float(input())
d = float(input())

area = heron(s1, s2, d) + heron(s3, s4, d)
print(area)