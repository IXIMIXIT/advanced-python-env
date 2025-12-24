# 8.1: Divisible by each of its digits
print("--- Task 8.1: Digit Divisors ---")
n = int(input("Enter n: "))
res = []
for i in range(1, n + 1):
    digits = [int(d) for d in str(i) if d != '0']
    if len(digits) == len(str(i)) and all(i % d == 0 for d in digits):
        res.append(i)
print(res)

# 8.2: Swap first and last elements
def swap_elements(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

print("\n--- Task 8.2: Swap Ends ---")
m = int(input("Array length: "))
a = [input(f"Elem {i+1}: ") for i in range(m)]
print(f"Original: {a}")
swap_elements(a)
print(f"Modified: {a}")