import math

# 3.1: Calculate and compare hypotenuses
def get_hypo(a, b):
    return math.sqrt(a**2 + b**2)

print("--- Task 3.1: Hypotenuse Comparison ---")
h1 = get_hypo(float(input("Tri 1 Leg A: ")), float(input("Tri 1 Leg B: ")))
h2 = get_hypo(float(input("Tri 2 Leg A: ")), float(input("Tri 2 Leg B: ")))
print(f"H1: {h1:.2f}, H2: {h2:.2f}")
print("H1 is greater" if h1 > h2 else "H2 is greater" if h2 > h1 else "Equal")

# 3.2: Sort letters in each word alphabetically
print("\n--- Task 3.2: Word Letter Sort ---")
text = input("Enter string: ")
print(" ".join(["".join(sorted(word)) for word in text.split()]))