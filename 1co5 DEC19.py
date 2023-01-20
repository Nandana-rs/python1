# program to read file content and store it into a list
# using readlines()
open_file = open("data2.txt" , 'r')
file_lines = open_file.readlines()

# without using strip function
print("\nFile content:")
print(file_lines)

# By using strip function
print("\nFile content after removing newline character:")
file_lines = [x.strip() for x in file_lines]
print([x.strip() for x in file_lines])

open_file.close()