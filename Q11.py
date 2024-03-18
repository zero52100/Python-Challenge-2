class InvalidDiscountError(Exception):
    pass
def calculate_discounted_price(mrp, discount, age):
    if discount < 0:
        raise InvalidDiscountError("Discount percentage cannot be negative.")
    if age < 18:
        discount += 1   
    discount = mrp * (discount / 100)
    discounted_price = mrp - discount
    return discounted_price
try:
    item_name=input("Enter the item name:-")
    mrp=float(input("Enter the MRP prcie of the product:-"))
    discount=float(input("Enter the discount percentage of the product:-"))
    age=int(input("Please enter your age (!if your age is less than 18, you will get a student discount of extra 1%):"))
    discounted_price = calculate_discounted_price(mrp, discount, age)
    print(f"The discounted price for {item_name} is: ${discounted_price:.2f}")
except ValueError:
    print("Error: Please enter valid numerical values.")
except InvalidDiscountError as e:
    print(f"Error: {e}")