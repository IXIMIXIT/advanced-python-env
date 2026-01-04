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

