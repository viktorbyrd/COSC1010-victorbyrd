#
# Victor Byrd
# 9-24-25
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# km to miles conversion factor
conversion_factor = 0.6214

def main():
    # get distance from user in km
    kilometers = float(input("Enter the distance in kilometers: "))

    # show km in miles
    show_miles(kilometers)

def show_miles(km):
    # calculate the miles
    miles = km * conversion_factor

    # display the results in miles (3 decimal places)
    print(km, "kilometers equals", format(miles, ".3f"), "miles.")

main()
