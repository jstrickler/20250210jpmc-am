MAX_TICKETS = 16

print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        print("Please enter # of tickets")
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    quantity = int(raw_quantity)  # could validate via try/except
    if quantity > MAX_TICKETS:
        print(f"Sorry, maximum purchase is {MAX_TICKETS} tickets")
        continue
    if quantity < 1:
        print("please purchase at least one ticket")
        continue
    print(f"sending {quantity} ticket(s)")
