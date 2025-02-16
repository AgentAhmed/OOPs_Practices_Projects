# An airline needs to decide which flight to book overbooked passengers on. the program is randomly assigning one of three flight or from multiple flights to each guest

# import random

# # List of overbooked passengers
# passengers = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"]

# # Available flights
# flights = ["Flight A", "Flight B", "Flight C"]

# # Assign each passenger to a random flight
# assignments = {passenger: random.choice(flights) for passenger in passengers}

# # Display assignments
# for passenger, flight in assignments.items():
#     print(f"{passenger} has been assigned to {flight}")

from random import randint 

passenger = input("Enter the name of the passenger ( quit to quit) : ").capitalize()

while passenger != "Quit":
    flight_number = randint(1,3)
    print(f"{passenger} has been assigned to Flight {flight_number}")
    passenger = input("Enter the name of the passenger ( quit to quit) : ").capitalize()

