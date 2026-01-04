# 3.2: Sort letters in each word alphabetically
print("\nTask 3.2: Word Letter Sort")
s = input().strip()
words = s.split()
res = ["".join(sorted(w)) for w in words]
print(" ".join(res))