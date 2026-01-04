# 8.1: Divisible by each of its digits
print("Task 8.1: Digit Divisors")
n = int(input())
for i in range(1, n + 1):
    d_list = [int(d) for d in str(i) if d != '0']
    if all(i % d == 0 for d in d_list):
        print(i)



