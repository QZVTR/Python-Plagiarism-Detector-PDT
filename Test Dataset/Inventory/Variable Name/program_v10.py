class Bag:
    """Class to represent an inventory system."""

    def __init__(self):
        self.items = {}

    def plus_item(self, x, yQuant):
        """Add an item to the inventory."""
        if x in self.items:
            self.items[x] += yQuant
        else:
            self.items[x] = yQuant
        print(f"{yQuant} {x}(s) added to the inventory.")

    def subtract_item(self, f, g):
        """Remove an item from the inventory."""
        if f in self.items and self.items[f] >= g:
            self.items[f] -= g
            print(f"{g} {f}(s) removed from the inventory.")
        else:
            print("Insufficient quantity or item not found in the inventory.")

    def show_inventory(self):
        """Display all items in the inventory."""
        if self.items:
            print("Inventory:")
            for t, quantity in self.items.items():
                print(f"{t}: {quantity}")
        else:
            print("Your inventory is empty.")

    def check_stock(self, hu):
        """Check the quantity of a specific item in the inventory."""
        if hu in self.items:
            print(f"Quantity of {hu}: {self.items[hu]}")
        else:
            print("Item not found in the inventory.")

    def gain_stock_item(self, nm, number):
        """Restock a specific item in the inventory."""
        if nm in self.items:
            self.items[nm] += number
            print(f"{number} {nm}(s) restocked.")
        else:
            print("Item not found in the inventory.")

    def get_rid_items(self):
        """Remove items with zero quantity from the inventory."""
        full_items = [item for item, quantity in self.items.items() if quantity == 0]
        for item in full_items:
            del self.items[item]
        print("Empty items removed from the inventory.")

    def sum_items(self):
        """Calculate the total number of items in the inventory."""
        minimum = sum(self.items.values())
        print(f"Total number of items: {minimum}")

    def update_item_quantity(self, item, new_quantity):
        """Update the quantity of a specific item in the inventory."""
        if item in self.items:
            self.items[item] = new_quantity
            print(f"Quantity of {item} updated to {new_quantity}")
        else:
            print("Item not found in the inventory.")

    def locate_item_by_quanity(self, number):
        """Find items with a specific number in the inventory."""
        located_items = [item for item, quant in self.items.items() if quant == number]
        if located_items:
            print(f"Items with quantity {number}: {', '.join(located_items)}")
        else:
            print("No items found with the specified quantity.")


def main():
    inv = Bag()

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
        pick = input("Enter your choice: ")

        if pick == "1":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to add: "))
            inv.plus_item(item, quantity)
        elif pick == "2":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to remove: "))
            inv.subtract_item(item, quantity)
        elif pick == "3":
            inv.show_inventory()
        elif pick == "4":
            item = input("Enter the item name: ")
            inv.check_stock(item)
        elif pick == "5":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to restock: "))
            inv.gain_stock_item(item, quantity)
        elif pick == "6":
            inv.get_rid_items()
        elif pick == "7":
            inv.sum_items()
        elif pick == "8":
            item = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            inv.update_item_quantity(item, new_quantity)
        elif pick == "9":
            quantity = int(input("Enter the quantity to search for: "))
            inv.locate_item_by_quanity(quantity)
        elif pick == "10":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
