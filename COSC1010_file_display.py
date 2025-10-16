#
# Victor Byrd
# 10-16/25
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# open  file
myfile = open ('numbers.txt', 'r')

# read and display
for line in myfile:
    numbers = int(line)
    print(numbers)

#close file
myfile.close()