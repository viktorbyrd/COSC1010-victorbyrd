#
# victor byrd
# 10-22-25
# Exception Handling Programming Project
# COSC 1010
#

def main():
    try:
        # open the file
        myfile = open('numbers.txt', 'r')
    except IOError:
        print("Error: could not open the file 'numbers.txt'. Please check if it exists.")
        return  # stop the program if file not found

    total = 0
    count = 0

    # try reading and converting data
    try:
        for line in myfile:
            try:
                number = int(line)
                total += number
                count += 1
            except ValueError:
                print(f"Warning: skipping invalid data '{line.strip()}' (not a number).")

        # Avoid dividing by 0
        if count > 0:
            average = total / count
            print(f"The average is: {average}")
        else:
            print("No valid numbers found in the file.")
    finally:
        # close the file
        myfile.close()

# call main function
main()
