def Secondlargest(num_list):
    if len(num_list) < 2:
        return "List must have at least two numbers for finding seacond largest number"
    
    sorted_number = sorted(set(num_list), reverse=True)
    return sorted_number[1]
   
try:
    limit=int(input("Enter the number string to list :"))
    num_list=[]
    for i in range(limit):
        item=int(input(f"Enter the {i+1}th string"))
        num_list.append(item)
    print(num_list)
    print(Secondlargest(num_list))
except ValueError:
    print("Error: Please enter a valid number for the limit.")