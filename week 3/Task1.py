import math

# 1.1: Calculate area of various geometric shapes
print("--- Task 1.1: Geometric Areas ---")
shape = input("Choose shape (1-Circle, 2-Rectangle, 3-Triangle): ")
if shape == '1':
    r = float(input("Radius: "))
    print(f"Area: {math.pi * r**2:.2f}")
elif shape == '2':
    l, w = float(input("Length: ")), float(input("Width: "))
    print(f"Area: {l * w}")
elif shape == '3':
    b, h = float(input("Base: ")), float(input("Height: "))
    print(f"Area: {0.5 * b * h}")

# 1.2: Sum and arithmetic mean of 3 arrays
print("\n--- Task 1.2: Array Stats ---")
arrays = [[1, 2, 3, 4, 5], [10, 20, 30], [5, 5, 5, 5]]
for i, arr in enumerate(arrays, 1):
    s = sum(arr)
    print(f"Array {i}: Sum = {s}, Mean = {s/len(arr):.2f}")