print("Welcome to the Inventory Manager!\n")

inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

def display_inventory():
    print("\nCurrent inventory:")
    for item, (qty, price) in inventory.items():
        print(f"Item: {item}, Quantity: {qty}, Price: ${price}")

def calculate_total_value():
    total = sum(qty * price for qty, price in inventory.values())
    print(f"\nTotal value of inventory: ${total:.2f}")

def add_item(name, qty, price):
    if name in inventory:
        print(f"{name} already exists. Use update to change quantity or price.")
    else:
        inventory[name] = (qty, price)
        print(f"{name} added successfully!")

def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print(f"{name} not found in inventory.")

def update_item(name, qty=None, price=None):
    if name in inventory:
        current_qty, current_price = inventory[name]
        new_qty = qty if qty is not None else current_qty
        new_price = price if price is not None else current_price
        inventory[name] = (new_qty, new_price)
        print(f"{name} updated successfully!")
    else:
        print(f"{name} not found in inventory.")

while True:
    print("\nOptions: display | add | remove | update | total | exit")
    choice = input("What would you like to do? ").strip().lower()

    if choice == "display":
        display_inventory()

    elif choice == "add":
        name = input("Enter item name to add: ").strip()
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        add_item(name, qty, price)

    elif choice == "remove":
        name = input("Enter item name to remove: ").strip()
        remove_item(name)

    elif choice == "update":
        name = input("Enter item name to update: ").strip()
        update_field = input("Update quantity (q), price (p), or both (b)? ").strip().lower()
        if update_field == "q":
            qty = int(input("Enter new quantity: "))
            update_item(name, qty=qty)
        elif update_field == "p":
            price = float(input("Enter new price: "))
            update_item(name, price=price)
        elif update_field == "b":
            qty = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            update_item(name, qty=qty, price=price)

    elif choice == "total":
        calculate_total_value()

    elif choice == "exit":
        print("Exiting Inventory Manager. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
