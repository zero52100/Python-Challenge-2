def sort(strings):
    sorted_strings = sorted(strings, key=len, reverse=True)
    print(type(sorted_strings))
    return sorted_strings
try:
    limit=int(input("Enter the number string to list :"))
    strings=[]
    for i in range(limit):
        item=input(f"Enter the {i+1}th string")
        strings.append(item)
    print(strings)
    print(sort(strings))
except ValueError:
    print("Error: Please enter a valid number for the limit.")
