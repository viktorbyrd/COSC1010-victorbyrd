#
# VictorByrd
# 9/11/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
#
# Get length A
length1 = int(input('Enter the length of rectangle 1: '))
# Get width A
width1 = int(input('Enter the width of rectangle 1: '))
# Get length B
lenght2 = int(input('Enter the lenght of rectangle 2: '))
# Get width B
width2 = int(input('Enter the width of rectangle 2: '))
# Calculate area A
area1 = length1 * width1
# Calculate area B
area2 = lenght2 * width2
# Print area comparison using if-elif-else statements
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')