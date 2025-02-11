fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[4] = }")
print(f"{fruits[21] = }")
print(f"{fruits[len(fruits) - 1] = }")
print(f"{fruits[-1] = }")
print(f"{fruits[-2] = }")
print()

# LIST[START-AT:STOP-BEFORE]
print(f"{fruits[0:5] = }")
start = 4
print(f"{fruits[start:start + 3] = }")
print(f"{fruits[:5] = }")
print(f"{fruits[15:] = }")
print(f"{fruits[:] = }")
print(f"{fruits[::] = }")
print(f"{fruits[3:15:2] = }")
print(f"{fruits[-4:] = }")

lunch = "spaghetti and meat balls"
print(f"{lunch[5:9] = }")
print(f"{lunch[-10:-6] = }")

a = "an apple is an apple and really is an apple"

misc_fruits = ["apple", "apple", "grape", "lemon", "apple", "apple", "apple", "banana", "apple", ]
# misc_fruits[100] = "watermelon"

non_apples = [f for f in misc_fruits if f != "apple"]
print(f"{non_apples = }")

# similar to foreach in some languages
# for VAR in ITERABLE:
for fruit in fruits:
    print(fruit.title())

