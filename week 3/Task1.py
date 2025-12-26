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

arrays = [[1, 2], [3, 4, 5]]
for arr in arrays:
    s = sum(arr)
    m = s / len(arr)
    print(s, m)


# 1.2: Sum and arithmetic mean of 3 arrays
print("\nTask 1.2: Array Stats")
arrays = [[1, 2], [3, 4, 5]]
for arr in arrays:
    s = sum(arr)
    m = s / len(arr)
    print(s, m)
