import math

# 2.1: Area of regular hexagon using triangle subroutine
print("Task 2.1: Hexagon Area")
def tri_area(a):
    return (math.sqrt(3) / 4) * a**2

side = float(input())
print(6 * tri_area(side))



