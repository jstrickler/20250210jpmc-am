
try:
    x = 5
    y = "cheese"
    # raise ValueError("that was the wrong type")
    z = x + y  # TypeError
    f = open("sesame.txt")  # IOError
    print("Bottom of try")

except (IOError, TypeError) as err:  # Use a tuple of 2 or more exception types
    print("Naughty programmer! ", err)
    raise

except Exception as err:
    print(f"Unexpected error {err} -- shutting down")
    exit()
