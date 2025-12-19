ticket = input()

first_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
last_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if first_sum == last_sum:
    print("YES")
else:
    print("NO")
