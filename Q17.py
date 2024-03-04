import time
def input_file(user_filename):
    content = []
    print("Enter content for the file (press Enter on an empty line to finish):")
    while True:
        data = input()
        if not data:
            break
        content.append(data)

    with open(user_filename, 'w') as original_file:
        original_file.write('\n'.join(content))
def print_with_delay(filename, delay):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
            time.sleep(delay)
user_filename = input("Enter the file name: ")
input_file(user_filename)
delay_time = float(input("Enter the delay time between lines (in seconds): "))
print_with_delay(user_filename , delay_time)
