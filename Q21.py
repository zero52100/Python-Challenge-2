def view_value_at_index(num_list, index):
    try:
        value = num_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print("Index is out of range. Please provide a valid index.")
limit = int(input("Enter the number of elements in the list: "))
num_list = []

for i in range(limit):
    item = int(input(f"Enter number to store at the {i}th index: "))
    num_list.append(item)
index_to_view = int(input("Enter the index to view: "))
view_value_at_index(num_list, index_to_view)
