while True:
    try:
        user_input = int(input("Enter your age : "))
        print(f"Age:{user_input}")
        break
    except ValueError:
        print("Invalid Input. Please Input Integer Only.")
