import csv

# -------------------------------------------------------
# Load inventory.csv into a list of dictionaries
# -------------------------------------------------------
def load_inventory(filename="inventory.csv"):
    inventory = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["quantity"]   = int(row["quantity"])
            row["unit_price"] = float(row["unit_price"])
            inventory.append(row)
    return inventory


# -------------------------------------------------------
# Compute total stock value for one item
# total_value = quantity * unit_price
# -------------------------------------------------------
def calc_item_value(item):
    return item["quantity"] * item["unit_price"]


# -------------------------------------------------------
# Display all records
# -------------------------------------------------------
def display_all_records(inventory):
    print(f"\n{'ID':<6} {'Name':<20} {'Category':<12} {'Qty':>6} {'Unit Price':>11} {'Total Value':>12}")
    print("-" * 72)
    for item in inventory:
        val = calc_item_value(item)
        print(f"{item['id']:<6} {item['name']:<20} {item['category']:<12} {item['quantity']:>6} {item['unit_price']:>11.2f} {val:>12.2f}")


# -------------------------------------------------------
# REQ-01: Return a list of items whose quantity is
#         STRICTLY LESS than the given threshold.
#         Return [] if no items are low stock or list empty.
# -------------------------------------------------------
def get_low_stock_items(inventory, threshold):
    # TODO: Implement this function
    if not inventory:
        return None
    low_stock = []
    for item in inventory:
        if int(item["quantity"]) < threshold:
            low_stock.append(item)
    return low_stock


# -------------------------------------------------------
# REQ-02: Return a list of items belonging to the given
#         category (case-insensitive match).
#         Return [] if none found or list is empty.
# -------------------------------------------------------
def get_items_by_category(inventory, category):
    # TODO: Implement this function
    if not inventory:
        return None
    
    category_item = []
    for item in inventory:
        if item["category"] == category:
            category_item.append(item)

    return category_item


# -------------------------------------------------------
# REQ-03: Return the total stock value across ALL items.
#         (sum of quantity * unit_price for every item)
#         Return 0 if list is empty.
# -------------------------------------------------------
def calc_total_stock_value(inventory):
    # TODO: Implement this function
    if not inventory:
        return None
    total_value = 0
    for item in inventory:
        stock_value = calc_item_value(item)
        total_value = total_value + stock_value

    return total_value


# -------------------------------------------------------
# REQ-04: Return the item with the HIGHEST total value
#         (quantity * unit_price). Return None if empty.
# -------------------------------------------------------
def get_highest_value_item(inventory):
    # TODO: Implement this function

    if not inventory:
        return None
    highest_value = None
    for item in inventory:
        stock_value = calc_item_value(item)
        if highest_value is None or stock_value > highest_value: 
            highest_value = stock_value
            top_item = item 

    return top_item

        


# -------------------------------------------------------
# Display statistics (calls REQ-03 and REQ-04)
# -------------------------------------------------------
def display_statistics(inventory):
    total = calc_total_stock_value(inventory)
    top   = get_highest_value_item(inventory)
    print(f"\nTotal stock value : ${total:.2f}")
    if top:
        print(f"Highest value item: {top['name']} (${calc_item_value(top):.2f})")


# -------------------------------------------------------
# Display low stock (calls REQ-01)
# -------------------------------------------------------
def display_low_stock(inventory):
    threshold = int(input("Enter low-stock threshold: "))
    items = get_low_stock_items(inventory, threshold)
    if not items:
        print(f"\nNo items below threshold {threshold}.")
    else:
        print(f"\nLow stock items (qty < {threshold}):")
        for item in items:
            print(f"  {item['name']} — Qty: {item['quantity']}")


# -------------------------------------------------------
# Display items by category (calls REQ-02)
# -------------------------------------------------------
def display_by_category(inventory):
    cat = input("Enter category: ").strip()
    items = get_items_by_category(inventory, cat)
    if not items:
        print(f"\nNo items found in category '{cat}'.")
    else:
        print(f"\nItems in '{cat}':")
        for item in items:
            print(f"  {item['name']} — Qty: {item['quantity']}, Price: ${item['unit_price']:.2f}")


# -------------------------------------------------------
# Main menu
# -------------------------------------------------------
def main():
    inventory = load_inventory()
    while True:
        print("\n" + "=" * 42)
        print("====== Inventory Manager ======")
        print("=" * 42)
        print("Select option")
        print("1 - Display all records")
        print("2 - Display statistics")
        print("3 - Display low stock items")
        print("4 - Display items by category")
        print("Q - Quit")
        print("=" * 42)
        choice = input("Enter selection => ").strip().upper()

        if choice == "1":
            display_all_records(inventory)
        elif choice == "2":
            display_statistics(inventory)
        elif choice == "3":
            display_low_stock(inventory)
        elif choice == "4":
            display_by_category(inventory)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
