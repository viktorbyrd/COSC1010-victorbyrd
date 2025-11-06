#
# Victor Byrd
# 11-5-25
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def main():
    # Get string 
    user_str = input ('Enter a string of characters: ')

    # Show the numbers of vowels and consonants
    print('The string has', num_vowels(user_str), 'vowels and', num_consonants(user_str), 'consonants')

# The num_vowels function returns the # of vowels in the string passed 
def num_vowels(s):
    # list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Start the counter
    v_count = 0

    # count the vowels
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # Return the vowel count
    return v_count

# The num_consonants return the # of consonants in the string passed
def num_consonants (s):
    # list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Start the counter
    c_count = 0

    # Count the consonants
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1

    # return the consonants count
    return c_count

main()