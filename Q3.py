def search(filename,Search_string):
    count=0
    check=0
    with open(filename,'r')as fileread:
        for line in fileread:
            for word in line.split():
                if Search_string == word.strip():
                    check =1
                    count +=1

    return check,count
filename = input("Enter the file name: ")
content = []
print("Enter content (press Enter on an empty line to finish):")
while True:
    data = input()
    if not data:
        break
    content.append(data)

with open(filename, 'w') as fileinsert:
    fileinsert.write('\n'.join(content))

Search_string = input("Enter the string to search in file: ")
check,count=search(filename,Search_string)
if check==1:
    print(f"the found and it appear {count} times in the file")
else:
    print("not found")