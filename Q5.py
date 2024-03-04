filename = input("Enter the name of the text file: ")
word_count = {}
try:
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    print(f"\nWord occurrences in the file '{filename}':")
    for word, count in word_count.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
