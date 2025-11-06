#
# Victor Byrd
# 10-27-25
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

import random  # import the random module

def main():
    try:
        # open file with possible answers
        with open('8_ball_responses.txt', 'r') as file:
            responses = [line.strip() for line in file.readlines()]  # strip removes \n
    except IOError:
        print("Error: could not open '8_ball_responses.txt'. Please check if the file exists.")
        return  # exit if file cannot be opened

    print("Welcome to the magic 8 ball!")
    print("Ask me a yes or no question (or type 'quit' to stop).")

    while True:
        # get the question
        question = input("\nWhat is your question? ")

        # check if user wants to quit
        if question.lower() == "quit":
            print("Goodbye! Come back when you seek more answers.")
            break

        # pick a random choice
        answer = random.choice(responses)

        # display the response
        print("The magic 8 ball says:", answer)

# run main function
main()
