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

# 3.2: Sort letters in each word alphabetically
print("\nTask 3.2: Word Letter Sort")
s = input().strip()
words = s.split()
res = ["".join(sorted(w)) for w in words]
print(" ".join(res))
