def is_perfect_square(num):
    if num >= 0:
        sqrt_num = int(num ** 0.5)
        if sqrt_num ** 2 == num:
            return True
    return False
def perfect_squares(num_list):
    squares = []
    non_squares = []
    for num in num_list:
        if is_perfect_square(num):
            squares.append(num)
        else:
            non_squares.append(num)
    return squares, non_squares
try:
    limit = int(input("Enter the number of strings to list: "))
    num_list = []

    for i in range(limit):
        item = int(input(f"Enter the {i + 1}th number: "))
        num_list.append(item)
    squares, non_squares = perfect_squares(num_list)
    print("Original list:", num_list)
    print("Perfect square in list:", squares)
    print("Non perfect square  in list:", non_squares)
   

except ValueError:
    print("Error: Please enter a valid number for the limit.")
