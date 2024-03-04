def merge_files(merge_filename, input_filenames):
    with open(merge_filename, 'w') as output_file:
        for input_filename in input_filenames:
            try:
                with open(input_filename, 'r') as input_file:
                    output_file.write(input_file.read() + '\n')
            except FileNotFoundError:
                print(f" !! Warning: File '{input_filename}' not found.")
merge_filename = input("Enter the name of the merged file: ")
input_filenames = []
while True:
    input_filename = input("Enter the name of the input file !press Enter to finish: ")
    if not input_filename:
        break
    input_filenames.append(input_filename)
if input_filenames:
    merge_files(merge_filename, input_filenames)
    print(f"\nFiles merged successfully into '{merge_filename}'.")
else:
    print("No input files provided.")
