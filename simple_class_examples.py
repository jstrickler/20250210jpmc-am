cities = list()   # []
cities.append("Durham")
cities.append("Houston")
cities.append("Jersey City")
cities.insert(2, "Dallas")
print(f"{list = }")
print(f"{type(cities) = }")

# list cities = new list(); 

class Dog:
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d2 = Dog()
print(f"{type(d1) = }")
print(f"{d2 = }")
d1.bark()
d2.bark()
