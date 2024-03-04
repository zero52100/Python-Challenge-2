def get_user_input(prompt, data_type, error_message="Invalid input. Please try again."):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print(error_message)
