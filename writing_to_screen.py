value = 8.389238923
name = "Ferd Berfel"
city = "Glasgow"

print(value)
print(name)
print(name, city)  # str(name) + " " + str(city) + "\n"
print(name, city, sep="/")
print(name, city, sep=", ")
print(name, city, sep="##")
print(name, end=" ")
print(city)
#  name: city
s = f"{name}: {city}"
print(s)

print("{name} lives in {city.upper()}")
print(f"{name} lives in {city.upper()}")
print(f"2 + 2 is {2 + 2}")
