my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()




my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()



# Open the file for reading
read_file = open("text.txt", "r")
# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()
# Try to read from the file
print read_file.read()
read_file.close()



with open("text.txt", "w") as textfile:
	textfile.write("Success!")
