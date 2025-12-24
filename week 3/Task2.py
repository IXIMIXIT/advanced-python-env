import math

# 2.1: Area of regular hexagon using triangle subroutine
def triangle_area(a):
    return (math.sqrt(3) / 4) * (a**2)

print("--- Task 2.1: Hexagon Area ---")
side = float(input("Enter side a: "))
print(f"Hexagon Area: {6 * triangle_area(side):.2f}")

# 2.2: Area of three rectangles
print("\n--- Task 2.2: Three Rectangles ---")
for i in range(1, 4):
    a = float(input(f"Rect {i} side 1: "))
    b = float(input(f"Rect {i} side 2: "))
    print(f"Area: {a * b}")