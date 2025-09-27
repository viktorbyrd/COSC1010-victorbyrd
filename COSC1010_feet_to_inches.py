#
# Victo Byrd
# 9-24-25
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

#constant for one foot
inches_per_foot = 12

def main():
    # get number of feet the user asked
    feet = int(input('Enter the number of feet: '))

    # convert feet to inches
    print(feet, "equals", feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * inches_per_foot

main()
