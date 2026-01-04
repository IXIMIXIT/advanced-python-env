# 8.2: Swap first and last elements
print("\nTask 8.2: Swap Ends")
def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input())
a = [int(input()) for _ in range(m)]
print(a)
swap(a)
print(a)