#
# Victor Byrd
# 10-21-25
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

import random

number = 7  # number of digits to generate
begin = 0   # lowest number that can be generated
end = 9     # highest number that can be generated

# main function
def main():
    # list
    numbers = [0] * number

    # generate numbers for list
    for index in range(number):
        numbers[index] = random.randint(begin, end)

    # display the results
    print('Here are your lottery numbers:')
    for index in range(number):
        print(numbers[index], end='')
    print()  # move to a new line after printing numbers

# call main
main()
