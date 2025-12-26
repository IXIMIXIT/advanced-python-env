items = input().split()
counts = {}

for x in items:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

print("Purchase frequency:")
for name in counts:
    print(name + ": " + str(counts[name]))

most_popular = ""
highest = 0
for name in counts:
    if counts[name] > highest:
        highest = counts[name]
        most_popular = name

print("Most popular item: " + most_popular)

once = []
for name in counts:
    if counts[name] == 1:
        once.append(name)
print("Purchased once: " + " ".join(once))