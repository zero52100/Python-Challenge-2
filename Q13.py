def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def expon(num1, num2):
    return num1 ** num2

while True:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Exit")

    user_choice = int(input("Enter your choice (1-6): "))

    if user_choice == 6:
        print("Exiting the program.")
        break

    if 1 <= user_choice <= 5:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_choice == 1:
            print("Result:", add(num1, num2))
        elif user_choice == 2:
            print("Result:", sub(num1, num2))
        elif user_choice == 3:
            print("Result:", mult(num1, num2))
        elif user_choice == 4:
            print("Result:", div(num1, num2))
        elif user_choice == 5:
            print("Result:", expon(num1, num2))

        continue_option = input("Do you want to continue? (y/n): ").lower()
        if continue_option != 'y':
            print("Exiting the program.")
            break
    else:
        print("Invalid choice!! Please enter a number between 1 and 6.")
