import math

# 1.1: Calculate area of various geometric shapes
print("Task 1.1: Geometric Areas")
import math

shape = input().strip()
if shape == '1':
    r = float(input())
    print(math.pi * r**2)
elif shape == '2':
    l = float(input())
    w = float(input())
    print(l * w)

