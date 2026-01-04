# 5.2: All divisors of a number
print("\nTask 5.2: Divisors")
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")