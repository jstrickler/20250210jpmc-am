value = 56

# if elif else while for def class with try except finally 

# structured pattern matching

if value > 75:
    print("wombat")
    print("wallaby")
elif value > 50:  # else if
    print("platypus")
else:
    print("koala")
    print("kangaroo")

print("ALL DONE")

# if EXPR
x = "wombat"
if x:
    print("x is true")

# C/Java/C# etc A ? B : C
# Python   B if A else C

debug = True

color = "red" if debug else "green"
print(f"{color = }")

# == != > < >= <=


if (color == 'red') and (x == 'wombat'):
    print("huzzah!!")

if (color == 'pink') or (x == 'wombat'):
    print("hooray!!")