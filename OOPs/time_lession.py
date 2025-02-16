from time import * 

countdown_start = int(input("Enter the countdown time in seconds: "))
while countdown_start > 0:
    print(countdown_start)
    sleep(1)
    countdown_start -= 1
print("Time's up! countdown finished! after :" , countdown_start ,"seconds")    