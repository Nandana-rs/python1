# program to copy odd lines of one file to another
# opening files for reading and writing data

input_file = open('data2.txt')
output_file = open('WriteData.txt','w')

# copying contents from read_file to copy_data
copy_data = input_file.readlines()
print("\nActual file content is:")
print(copy_data,"\n")

for i in range (0,len(copy_data)):
    if i%2==0:
        output_file.write(copy_data[i])
    else:
        pass

# closing file after copying
output_file.close()

# opening write file in read mode and printing values
output_file = open('WriteData.txt','r')
print("\nOdd lines are:")
print(output_file.read())

#closing files
input_file.close()
output_file.close()