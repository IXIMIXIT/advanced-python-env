import sys

lines = sys.stdin.read().split()
N = int(lines[0])
valid_chars = "ABCEHKMOPTXY"

for i in range(1, N + 1):
    p = lines[i]
    if len(p) == 6 and p[0] in valid_chars and p[1:4].isdigit() and p[4] in valid_chars and p[5] in valid_chars:
        print("Yes")
    else:
        print("No")
