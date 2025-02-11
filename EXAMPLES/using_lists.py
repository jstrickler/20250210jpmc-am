cities = list() 
cities = []  # preferred

cities = ['Portland', 'Pittsburg', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")


cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)  # for city in more cities: cities.append(city)
print(f"cities: {cities}\n")

# LIST.apppend(OBJ)  LIST.insert(POS, OBJ)  LIST.extend(ITERABLE)

del cities[3]
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

#  del LIST[idx]   LIST.pop()  LIST.pop(idx)   LIST.remove("value")