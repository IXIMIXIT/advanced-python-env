# 8.1: Divisible by each of its digits
print("Task 8.1: Digit Divisors")
n = int(input())
for i in range(1, n + 1):
    d_list = [int(d) for d in str(i) if d != '0']
    if all(i % d == 0 for d in d_list):
        print(i)


# 8.2: Swap first and last elements
print("\nTask 8.2: Swap Ends")
def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input())
a = [int(input()) for _ in range(m)]
print(a)
swap(a)
print(a)
