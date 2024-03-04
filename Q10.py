
def divisible(num_list):
    sum =0
    nonsum=0
    for num in num_list:
        if num % 3==0 or num % 5==0:
            sum +=num
        else:
            nonsum +=num
    return sum, nonsum
try:
    limit = int(input("Enter the number of strings to list: "))
    num_list = []

    for i in range(limit):
        item = int(input(f"Enter the {i + 1}th number: "))
        num_list.append(item)
    sum, nonsum = divisible(num_list)
    print("Original list:", num_list)
    print("Sum of numbers divisible by 3 or 5:", sum)
    print("Sum of numbers non divisible by 3 or 5:", nonsum)
   

except ValueError:
    print("Error: Please enter a valid number for the limit.")
