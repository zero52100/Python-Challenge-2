def count_lines_words_characters(filename):
    no_of_lines = 0
    no_of_words = 0
    no_of_characters = 0

    with open(filename, 'r') as fileread:
        for line in fileread:
            no_of_lines += 1
            words = line.split()
            no_of_words += len(words)
            no_of_characters += sum(len(word) for word in words)

    return no_of_lines, no_of_characters, no_of_words

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

no_of_lines, no_of_characters, no_of_words = count_lines_words_characters(filename)
print(f"\nNumber of lines: {no_of_lines}")
print(f"Number of words: {no_of_words}")
print(f"Number of characters: {no_of_characters}")
