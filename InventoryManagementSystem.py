class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, category, quantity, price):
        if name in self.inventory:
            print(f"Item '{name}' already exists in the inventory.")
        else:
            self.inventory[name] = {
                'category': category,
                'quantity': quantity,
                'price': price
            }
            print(f"Item '{name}' added to the inventory.")

    def update_item(self, name, category=None, quantity=None, price=None):
        if name not in self.inventory:
            print(f"Item '{name}' not found in the inventory.")
        else:
            if category is not None:
                self.inventory[name]['category'] = category
            if quantity is not None:
                self.inventory[name]['quantity'] = quantity
            if price is not None:
                self.inventory[name]['price'] = price
            print(f"Item '{name}' updated successfully.")
            
    def delete_item(self, name):
        if name not in self.inventory:
            print(f"Item '{name}' not found in the inventory.")
        else:
            del self.inventory[name]
            print(f"Item '{name}' deleted from the inventory.")
            
    def view_items(self):
        if not self.inventory:
            print("No items in the inventory.")
        else:
            print("Inventory Items:")
            for name, details in self.inventory.items():
                print(f"Name: {name}, Category: {details['category']}, Quantity: {details['quantity']}, Price: {details['price']}")
                
    def search_item(self, name):
        if name in self.inventory:
            details = self.inventory[name]
            print(f"Item '{name}' found: Category: {details['category']}, Quantity: {details['quantity']}, Price: {details['price']}")
        else:
            print(f"Item '{name}' not found in the inventory.")
            
    def search_by_category(self, category):
        found_items = {name: details for name, details in self.inventory.items() if details['category'] == category}
        if not found_items:
            print(f"No items found in category '{category}'.")
        else:
            print(f"Items in category '{category}':")
            for name, details in found_items.items():
                print(f"Name: {name}, Quantity: {details['quantity']}, Price: {details['price']}")
                
    def main(self):
        while True:
            print("\nNIcholas' Inventory Management System Menu:")
            print("1. Add Item")
            print("2. Update Item")
            print("3. Delete Item")
            print("4. View Items")
            print("5. Search Item by Name")
            print("6. Search Items by Category")
            print("7. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                name = input("Enter item name: ")
                category = input("Enter item category: ")
                quantity = int(input("Enter item quantity: "))
                price = float(input("Enter item price: "))
                self.add_item(name, category, quantity, price)
            elif choice == '2':
                name = input("Enter item name to update: ")
                category = input("Enter new item category: ")
                quantity = input("Enter new item quantity: ")
                price = input("Enter new item price: ")
                self.update_item(name, category if category else None, int(quantity) if quantity else None, float(price) if price else None)
            elif choice == '3':
                name = input("Enter item name to delete: ")
                self.delete_item(name)
            elif choice == '4':
                self.view_items()
            elif choice == '5':
                name = input("Enter item name to search: ")
                self.search_item(name)
            elif choice == '6':
                category = input("Enter category to search items: ")
                self.search_by_category(category)
            elif choice == '7':
                print("Thank you for using my Inventory Management System.")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    inventory_system = InventoryManagementSystem()
    inventory_system.main()