def terminal_1():
    print("Your flight is departing from terminal 1")
    flight_check()
    
def terminal_2():
    print("Your flight is departing from terminal 2")
    flight_check()
    
def terminal_3():
    print("Your flight is departing from terminal 3")
    flight_check()
    
def flight_check():
    answer = input("Is your flight a budget/domestic or international  ").lower()
    if answer == "budget" :
        terminal_1()
    elif answer == "domestic":
        terminal_2()
    elif answer == "international":       
        terminal_3()           