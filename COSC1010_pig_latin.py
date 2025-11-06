#
# Victor Byrd
# 11-05-25
# Pig Latin Programming Project
# COSC 1010
#
# This program reads a sentence and converts each word into Pig Latin.
# In Pig Latin, you remove the first letter, move it to the end,
# then add "ay" to the word. Example: SLEEP -> LEEPSAY
#

def main():
    # Ask for english sentance in all caps
    sentence = input("Enter a sentence in English: ").upper()

    # Split sentance into words
    words = sentence.split()

    # list to store words
    pig_latin_words = []

    # Loop for each word to turn into pig latin
    for word in words:
        if len(word) > 1:
            # Move first and add ay
            pig_word = word[1:] + word[0] + "AY"
        else:
            # A and I 
            pig_word = word + "AY"

        pig_latin_words.append(pig_word)

    # Put all the new latin words together
    pig_sentence = " ".join(pig_latin_words)

    # Show the results
    print("\nPig Latin translation:")
    print(pig_sentence)



main()
