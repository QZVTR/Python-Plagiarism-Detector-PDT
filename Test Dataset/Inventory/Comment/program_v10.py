class Inventory:
    """Class to represent an inventory system."""

    # Comment 1
    def __init__(self):
        self.items = {}

    # Comment 2
    def add_item(self, item, quantity):
        """Add an item to the inventory."""
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"{quantity} {item}(s) added to the inventory.")

    # Comment 5
    def remove_item(self, item, quantity):
        """Remove an item from the inventory."""
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            print(f"{quantity} {item}(s) removed from the inventory.")
        else:
            print("Insufficient quantity or item not found in the inventory.")

    def display_inventory(self):
        """Display all items in the inventory."""
        if self.items:
            print("Inventory:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
        else:
            print("Your inventory is empty.")

    def check_item_quantity(self, item):
        """Check the quantity of a specific item in the inventory."""
        if item in self.items:
            print(f"Quantity of {item}: {self.items[item]}")
        else:
            print("Item not found in the inventory.")

    # Comment 6
    def restock_item(self, item, quantity):
        """Restock a specific item in the inventory."""
        if item in self.items:
            self.items[item] += quantity
            print(f"{quantity} {item}(s) restocked.")
        else:
            print("Item not found in the inventory.")

    def remove_empty_items(self):
        """Remove items with zero quantity from the inventory."""
        empty_items = [item for item, quantity in self.items.items() if quantity == 0]
        for item in empty_items:
            del self.items[item]
        print("Empty items removed from the inventory.")

    # Comment 7
    def total_items(self):
        """Calculate the total number of items in the inventory."""
        total = sum(self.items.values())
        print(f"Total number of items: {total}")

    def update_item_quantity(self, item, new_quantity):
        """Update the quantity of a specific item in the inventory."""
        if item in self.items:
            self.items[item] = new_quantity
            print(f"Quantity of {item} updated to {new_quantity}")
        else:
            print("Item not found in the inventory.")

    # Comment 8
    def find_item_by_quantity(self, quantity):
        """Find items with a specific quantity in the inventory."""
        found_items = [item for item, quant in self.items.items() if quant == quantity]
        if found_items:
            print(f"Items with quantity {quantity}: {', '.join(found_items)}")
        else:
            print("No items found with the specified quantity.")


# Comment 3
def main():
    inventory = Inventory()
    # Comment 4
    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Check Item Quantity")
        print("5. Restock Item")
        print("6. Remove Empty Items")
        print("7. Total Items")
        print("8. Update Item Quantity")
        print("9. Find Item by Quantity")
        print("10. Exit")
        choice = input("Enter your choice: ")
        # Comment 9
        if choice == "1":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to add: "))
            inventory.add_item(item, quantity)
        elif choice == "2":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to remove: "))
            inventory.remove_item(item, quantity)
        elif choice == "3":
            inventory.display_inventory()
        elif choice == "4":
            item = input("Enter the item name: ")
            inventory.check_item_quantity(item)
        elif choice == "5":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to restock: "))
            inventory.restock_item(item, quantity)
        elif choice == "6":
            inventory.remove_empty_items()
        elif choice == "7":
            inventory.total_items()
        elif choice == "8":
            item = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            inventory.update_item_quantity(item, new_quantity)
        elif choice == "9":
            quantity = int(input("Enter the quantity to search for: "))
            inventory.find_item_by_quantity(quantity)
        elif choice == "10":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
