def copy_and_input(user_filename, copy_file):
    content = []
    print("Enter content for the file (press Enter on an empty line to finish):")
    while True:
        data = input()
        if not data:
            break
        content.append(data)

    with open(user_filename, 'w') as original_file:
        original_file.write('\n'.join(content))

    lines_copied = 0
    with open(user_filename, 'r') as file_open:
        with open(copy_file, 'w') as open_file:
            for line_number, line in enumerate(file_open, start=1):
                if line_number % 2 != 0:
                    open_file.write(line)
                    lines_copied += 1

            if lines_copied == 0:
                print("File is empty. Cannot copy odd lines.")

user_filename = input("Enter the filename: ")
copy_file = input(f"Enter the filename to copy the odd lines from {user_filename} to: ")

copy_and_input(user_filename, copy_file)
with open(copy_file, 'r') as copied_file:
    copied_content = copied_file.read()
    print(copied_content)
