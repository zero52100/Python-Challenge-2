class Notes:
    @staticmethod
    def write(filename):
        user_input = input("Enter the note to overwrite the file: ")
        with open(filename, 'w') as file:
            file.write(user_input)
        print("Note written successfully.")

    @staticmethod
    def append(filename):
        user_input = input("Enter the note to append to the file: ")
        with open(filename, 'a') as file:
            file.write("\n" + user_input)
        print("Note appended successfully.")

    @staticmethod
    def read(filename):
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                if not contents:
                    return "No notes found."
                return contents
        except FileNotFoundError:
            return "No notes found."

filename = input("Enter the filename to store notes: ")

while True:
    print("\n1 - Write Note (Overwrite existing).")
    print("2 - Add more Notes (Append).")
    print("3 - Read Notes.")
    print("4 - Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        Notes.write(filename)
    elif choice == '2':
        Notes.append(filename)
    elif choice == '3':
        notes_content = Notes.read(filename)
        print("Notes:\n", notes_content)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
