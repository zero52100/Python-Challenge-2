class MenuItem:
    def __init__(self, name, price, description, category):
        self.name = name
        self.price = price
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.name} - ₹{self.price}\n{self.description}\n"
class Menu:
    def __init__(self):
        self.menu_items = []
    def add_item(self, item):
        self.menu_items.append(item)

    def display_menu(self, category):
        if not self.menu_items:
            print("No items in the menu.")
        else:
            print("Menu:")
            if category:
                for index, item in enumerate(self.menu_items, 1):
                    if item.category == category:
                        print(f"{index}. {item}")
            
    print("name")
def take_order(menu):
    order = []
    while True:
        print("\nSelect a category to order:")
        print("1. Desserts")
        print("2. Hot/Cold Beverages")
        print("3. Main Course")
        print("4. Finish Ordering")

        choice = input("Enter your choice (1-4): ")
        if choice == '4':
            break
        elif choice in {'1', '2', '3'}:
            category = {'1': 'Desserts', '2': 'Hot/Cold Beverages', '3': 'Main Course'}[choice]
            menu.display_menu(category)
            item_number = input(f"Enter the number of the {category} item you want to order: ")
            quantity = int(input("Enter the quantity: "))

            try:
                selected_item = menu.menu_items[int(item_number) - 1]
                order.append((selected_item, quantity))
                print(f"{quantity}x {selected_item.name} added to the order.")
            except (IndexError, ValueError):
                print("Invalid item number. Please enter a valid number.")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    return order
def calculate_total(order):
    total = 0
    for item, quantity in order:
        total += item.price * quantity
    return total
dessert1 = MenuItem("Blackforest Cake", 159, "Delicious chocolate cake.", "Desserts")
dessert2 = MenuItem("Cheesecake", 169, "Creamy cheesecake with raspberry sauce.", "Desserts")
beverage1 = MenuItem("Cappuccino", 30, "Hot brewed coffee.", "Hot/Cold Beverages")
beverage2 = MenuItem("Iced Tea", 40, "Refreshing iced tea.", "Hot/Cold Beverages")
main_course1 = MenuItem("Pizza", 289, "A hugely popular margherita, with a deliciously tangy single cheese topping.", "Main Course")
main_course2 = MenuItem("Grilled Chicken", 349, "Grilled chicken with pepper butter sauce.", "Main Course")
restaurant_menu = Menu()
restaurant_menu.add_item(dessert1)
restaurant_menu.add_item(dessert2)
restaurant_menu.add_item(beverage1)
restaurant_menu.add_item(beverage2)
restaurant_menu.add_item(main_course1)
restaurant_menu.add_item(main_course2)
order = take_order(restaurant_menu)
final_bill = calculate_total(order)

if final_bill == 0:
    print("No items ordered. Thank you!")
else:
    print("\nFinal Bill:")
    for item, quantity in order:
        print(f"{quantity}x {item.name} - ₹{item.price * quantity:.2f}")
    print(f"Total: ₹{final_bill:.2f}")
