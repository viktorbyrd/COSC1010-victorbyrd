#
# victor byrd
#10/16/25
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#open file
myfile = open('numbers.txt','r')

#initialize variable
total = 0
count = 0

#read and sum numbers
for line in myfile:
    total += int(line)
    count += 1

#close file
myfile.close()

#calculate and display the average
print(f'The average is: {total/count}')