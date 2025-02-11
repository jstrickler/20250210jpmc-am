
colors = "red blue green yellow brown black".split()

months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

enum_colors = enumerate(colors)
print(f"{enum_colors = }")

for i, color in enum_colors:  # enumerate() returns iterable of (index, value) tuples
    print(i, color)

print(f"{list(enumerate(colors)) = }")

print()

for num, month in enumerate(months, 1):  # Second parameter to enumerate is added to index
    print(f"{num} {month}")

colors_rev = reversed(colors)
print(f"{colors_rev = }")
for color in colors_rev:
    print(color)
print()

for i in range(5):
    print(i)
print()
# i = 0
# while i < 5:
#     print(i)
#     i += 1
