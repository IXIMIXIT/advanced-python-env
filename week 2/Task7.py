from collections import Counter

items = input().split()
counts = Counter(items)

print("Purchase frequency:")
for item, freq in counts.items():
    print(f"{item}: {freq}")

most_popular = counts.most_common(1)[0][0]
print(f"Most popular item: {most_popular}")

once = [item for item, freq in counts.items() if freq == 1]
print(f"Purchased once: {' '.join(once)}")

sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("Sorted by frequency:")
for item, freq in sorted_items:
    print(f"{item} {freq}")