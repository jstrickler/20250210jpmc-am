

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print(get_hello())
print()


#  func(param):
#     ...
def sqrt(num):  # Function takes exactly one argument
    return num ** .5

# func(arg)
m = sqrt(1234)  # Call function with one argument
n = sqrt(2)
x = 1000
print(sqrt(x))

print(f"m is {m:.3f} n is {n:.3f}")

def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 10))
print(f"{rectangle_area(.5, 37.4) = }")

def find_word(word, *files, ignore_case=False, **other_options):
    print(f"{other_options = }")
    
    if ignore_case:
        word = word.lower()
    for file in files:
        with open(file) as file_in:
            for raw_line in file_in:
                if ignore_case:
                    search_line = raw_line.lower()
                else:
                    search_line = raw_line
                if word in search_line:
                    print(file, raw_line.rstrip())

find_word('lizard', '../DATA/alice.txt', '../DATA/words.txt', ignore_case=True, animal='Wombat')
print('-' * 60)
find_word('wombat', '../DATA/words.txt')
