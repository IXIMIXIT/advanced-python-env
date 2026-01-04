import math

# 3.1: Calculate and compare hypotenuses
print("Task 3.1: Hypotenuse Comparison")
def get_h(a, b):
    return math.sqrt(a**2 + b**2)

h1 = get_h(float(input()), float(input()))
h2 = get_h(float(input()), float(input()))

if h1 > h2:
    print("First is greater")
else:
    print("Second is greater")


