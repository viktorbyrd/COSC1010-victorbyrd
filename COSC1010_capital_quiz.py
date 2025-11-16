#
# Victor Byrd
# 11-14-25
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

def state_cap_dictionary():
    # dictionary of u.s. states and capitals
    sc = {'Alabama':'Montgomery', 'Alaska':'Juneau',
          'Arizona':'Phoenix', 'Arkansas':'Little Rock',
          'California':'Sacramento', 'Colorado':'Denver',
          'Connecticut':'Hartford', 'Delaware':'Dover',
          'Florida':'Tallahassee', 'Georgia':'Atlanta',
          'Hawaii':'Honolulu', 'Idaho':'Boise',
          'Illinois':'Springfield', 'Indiana':'Indianapolis',
          'Iowa':'Des Moines', 'Kansas':'Topeka',
          'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
          'Maine':'Augusta', 'Maryland':'Annapolis',
          'Massachusetts':'Boston', 'Michigan':'Lansing',
          'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
          'Missouri':'Jefferson City', 'Montana':'Helena',
          'Nebraska':'Lincoln', 'Nevada':'Carson City',
          'New Hampshire':'Concord', 'New Jersey':'Trenton',
          'New Mexico':'Santa Fe', 'New York':'Albany',
          'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
          'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
          'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
          'Rhode Island':'Providence', 'South Carolina':'Columbia',
          'South Dakota':'Pierre', 'Tennessee':'Nashville',
          'Texas':'Austin', 'Utah':'Salt Lake City',
          'Vermont':'Montpelier', 'Virginia':'Richmond',
          'Washington':'Olympia', 'West Virginia':'Charleston',
          'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    
    return sc

# number of questions
NUM_STATES = 5

def main():
    # get the dictionary of states/capitals
    state_caps = state_cap_dictionary()

    # counter
    correct = 0
    incorrect = 0

    print("Capital Quiz! You will be asked", NUM_STATES, "states.\n")

    # Loop number of times
    for count in range(NUM_STATES):

        # get a random state/capital
        state, capital = state_caps.popitem()

        # ask for the capital
        print("What is the capital of", state + "?")
        response = input("Enter your answer: ")

        # check to see if it correct 
        if response.lower() == capital.lower():
            print("Correct!\n")
            correct += 1
        else:
            print("Incorrect. The correct answer is", capital + ".\n")
            incorrect += 1

    # show results
    print("Quiz Complete!")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)

main()
