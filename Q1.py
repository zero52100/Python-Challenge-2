filename=input("Enter the file name :")
fiecontent=input("Enter the file content")
with open(filename,'w') as createfile:
    input_data=input(f"Enter the data to {filename} :")
    createfile.write(input_data)
with open(filename,'r') as readfile:
    
    print(f"The content of {filename} is {readfile.read()} ")
