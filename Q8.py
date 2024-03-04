def checkprime(num_list):
    prime = []
    nonprime=[]
    for num in num_list:
        if num == 1:
            print(num, "is not a prime number")
            nonprime.append(num)
        elif num > 1:
            flag = False
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
            if not flag:
                prime.append(num)
            else:
                nonprime.append(num)

    return prime,nonprime

try:
    limit = int(input("Enter the number of strings to list: "))
    num_list = []

    for i in range(limit):
        item = int(input(f"Enter the {i + 1}th number: "))
        num_list.append(item)
    prime,nonprime=checkprime(num_list)
    print("Original list:", num_list)
    print("Prime numbers in the list:",prime )
    print("Prime numbers in the list:",nonprime )

except ValueError:
    print("Error: Please enter a valid number for the limit.")
