# 1.2: Sum and arithmetic mean of 3 arrays
print("\nTask 1.2: Array Stats")
arrays = [[1, 2], [3, 4, 5]]
for arr in arrays:
    s = sum(arr)
    m = s / len(arr)
    print(s, m)