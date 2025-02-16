from terminal import *

question  = input("Would you like to check your flight ? ").lower()
while question != 'quit':
    if question == 'yes':
        flight_check()
    else:
        print("You did not enter a valid response")
            
    question = input("Would you like to check your flight ? ").lower()