from input import get_user_input

name = get_user_input("Enter your name: ", str)
print(f"Hello, {name}!")

age = get_user_input("Enter your age: ", int, "Age must be a valid integer.")
print(f"Your age is: {age}")

height = get_user_input("Enter your height (in cm): ", float, "Height must be a valid floating-point number.")
print(f"Your height is: {height} cm")
