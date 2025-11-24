import json
from datetime import datetime

MENU_FILE = "menu_simple.json"
ORDER_LOG = "order_log_simple.txt"
TAX_RATE = 0.05


# Load Menu (or create default)
def load_menu():
    try:
        with open(MENU_FILE, "r") as f:
            return json.load(f)
    except:
        #menu
        menu = {
            "101": {"name": "Burger", "price": 120},
            "102": {"name": "Pizza Slice", "price": 90},
            "103": {"name": "Sandwich", "price": 70},
            "201": {"name": "Cold Drink", "price": 40},
            "301": {"name": "Chocolate Cake", "price": 60}
        }
        save_menu(menu)
        return menu


def save_menu(menu):
    with open(MENU_FILE, "w") as f:
        json.dump(menu, f, indent=4)


# ------------------------------
# Display Menu
# ------------------------------
def display_menu(menu):
    print("\n------ MENU ------")
    print("ID  | Item Name        | Price")
    print("------------------------------")
    for item_id in sorted(menu.keys()):
        item = menu[item_id]
        print(f"{item_id} | {item['name']:<15} | Rs{item['price']}")
    print("------------------------------")


# Start New Order
def start_order():
    return {}   # Empty dictionary for order items


# Add Item
def add_item(order, menu):
    item_id = input("Enter Item ID: ").strip()
    if item_id not in menu:
        print("Invalid Item ID!")
        return

    qty = input("Enter Quantity: ").strip()

    if not qty.isdigit() or int(qty) <= 0:
        print("Invalid quantity!")
        return

    qty = int(qty)

    # Add quantity
    if item_id in order:
        order[item_id] += qty
    else:
        order[item_id] = qty

    print(f"Added {qty} x {menu[item_id]['name']} to the order.")


# Final Bill
def finalize_bill(order, menu):
    if not order:
        print("\nOrder is empty! Nothing to finalize.")
        return

    print("\n------ FINAL BILL ------")
    subtotal = 0

    print("Qty | Item Name        | Price | Total")
    print("----------------------------------------")

    for item_id, qty in order.items():
        name = menu[item_id]["name"]
        price = menu[item_id]["price"]
        line_total = qty * price

        subtotal += line_total

        print(f"{qty:<3} | {name:<15} | {price:<5} | {line_total}")

    tax = subtotal * TAX_RATE
    grand = subtotal + tax

    print("----------------------------------------")
    print(f"Subtotal: Rs{subtotal:.2f}")
    print(f"Tax (5%): Rs{tax:.2f}")
    print(f"Grand Total: Rs{grand:.2f}")
    print("----------------------------------------")

    log_transaction(order, menu, grand)

    print("\nOrder saved! Thank you.")


# Log the transaction
def log_transaction(order, menu, total):
    entry = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": [],
        "total": total
    }

    for item_id, qty in order.items():
        entry["items"].append({
            "name": menu[item_id]["name"],
            "qty": qty,
            "price": menu[item_id]["price"]
        })

    with open(ORDER_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")


# MAIN MENU LOOP
def main():
    menu = load_menu()
    order = {}

    while True:
        print("\n============================")
        print(" SIMPLE RESTAURANT SYSTEM ")
        print("============================")
        print("1. Show Menu")
        print("2. Start New Order")
        print("3. Add Item")
        print("4. Finalize Bill")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_menu(menu)

        elif choice == "2":
            order = start_order()
            print("\nNew order started!")

        elif choice == "3":
            if not order:
                print("\nNo order started! Starting automatically...")
                order = start_order()
            display_menu(menu)
            add_item(order, menu)

        elif choice == "4":
            finalize_bill(order, menu)
            order = {}  # Reset after bill

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
