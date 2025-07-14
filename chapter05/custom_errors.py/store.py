# Custom exception class for when a product is out of stock
class outOfStockError(Exception):
    def __init__(self, item_name):
       
        # Calls the constructor of the base Exception class with a custom message
        super().__init__(f"{item_name} is out of stock.")

# Class that represents a product with a name and quantity
class Item:
    def __init__(self, name, quantity):
        self.name = name              # Stores the name of the product
        self.quantity = quantity      # Stores the quantity

    # Returns a string with the name and quantity when print() is used
    def __str__(self):
        return f"{self.name}, {self.quantity} "

    # Checks if two Item objects are considered equal
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False              # Returns False if 'other' is not an Item
        return self.name == other.name  # Items are equal if they have the same name

    # Allows Item objects to be used in sets or as dictionary keys
    def __hash__(self):
        return hash(self.name)        # The hash is based on the item's name

class Inventory:
    def __init__(self):

# Store items: key = item name, value = Item object

        self.items = []
    
    def add_items(self, item):
# If the item name already exists, increase its quantity

        for existing_item in self.items:
            if existing_item == item:
                existing_item.quantity += item.quantity
                return
            
        self.items.append(item)

    def remove_item(self, item_to_remove):
        if Item(item_to_remove, None) not in self.items:
            raise ValueError(f"{item_to_remove} is not in the inventory.")
        
        for item in self.items:

            if item == Item(item_to_remove, None):
    # Check if there's at least one item left

                if item.quantity > 0:
                    item.quantity -= 1
                    return Item(item.name, item.quantity)
                else:
                    raise outOfStockError(item.name)

    def print_items(self):
        for item in self.items:
            print(item)
        
def main():

    inventory = Inventory()
    inventory.add_items(Item("Book", 2))
    inventory.add_items(Item("Pen", 5))
    inventory.add_items(Item("Book", 3))

    print("Initial inventory: ")
    inventory.print_items()
    
    # Try to remove an item
    try:
        removed_item = inventory.remove_item("Book")
        print(f"\nRemoved one : {removed_item}")
    except (ValueError, outOfStockError) as e:
        print (f"Error: {e}")

    # Try to remove an item not in inventory
    try:
        removed_item = inventory.remove_item("Pencil")
    except ValueError as e:
        print(f"\nError: {e}")


    print("\nFinal inventory:")
    inventory.print_items()

if __name__ == "__main__":
    main()

