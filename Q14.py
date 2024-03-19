class Notes:
    def __init__(self, filename):
        self.filename = filename

    def write(self):
        user_input = input("Enter the note to overwrite the file: ")
        with open(self.filename, 'w') as file:
            file.write(user_input)
        print("Note written successfully.")

    def append(self):
        user_input = input("Enter the note to append to the file: ")
        with open(self.filename, 'a') as file:
            file.write("\n" + user_input)
        print("Note appended successfully.")

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                contents = file.read()
                if not contents:
                    return "No notes found."
                return contents
        except FileNotFoundError:
            return "No notes found."

filename = input("Enter the filename to store notes: ")
notes_instance = Notes(filename)

while True:
    print("\n1 - Write Note (Overwrite existing).")
    print("2 - Add more Notes (Append).")
    print("3 - Read Notes.")
    print("4 - Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        notes_instance.write()
    elif choice == '2':
        notes_instance.append()
    elif choice == '3':
        notes_content = notes_instance.read()
        print("Notes:\n", notes_content)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
