def count_uppercase(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    count += 1
    return count

filename = input("Enter the file name: ")
with open(filename, 'w') as createfile:
    input_data = input(f"Enter the data to {filename}: ")
    createfile.write(input_data)

no_capital = count_uppercase(filename)
if no_capital == 0:
    print(f"No uppercase characters found in the file {filename}.")
else:
    print(f"Total uppercase characters in the file {filename}: {no_capital}")

