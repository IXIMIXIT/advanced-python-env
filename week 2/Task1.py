def count_arrows(s):
    arrows = [">>-->", "<--<<"]
    count = 0
    for i in range(len(s) - 4):
        if s[i:i+5] in arrows:
            count += 1
    return count

s = input().strip()
print(count_arrows(s))