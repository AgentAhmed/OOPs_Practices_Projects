# def good_deal(cost):
#     if cost >= 50 and cost <= 150:
#         response = "This is a good deal!"
    
#     elif cost > 150:
#         response = "Overpriced!"    
        
#     else:
#         response = "This is too cheap!, buy now !"    
        
#     category = response     

# store = input("Enter the store name: ")
# cost = float(input("Enter the cost of the item: "))

# res = good_deal(cost)
# print(f"{store} is selling the item for {cost} and {res}")

# if res == "This is a good deal!":
#     print("Buy now!")


# def mortgage(cash):
#     if cash >= 50000:
#         print("Instant approval!")
#     elif cash < 50000 and cash >= 20000:
#         print("Approval pending!") 
        
#     else:
#         print("Declined!")
        
# cash = int(input("Deposit amount: "))    
# total_balance = 0 
# while cash != 0:
#     total_balance += cash
#     mortgage(cash)
#     cash = int(input("Deposit amount: "))     
    
# print("Total money requested: ", total_balance)       

# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     if bmi < 18.5:
#         category =  "Underweight"
#     elif bmi >= 18.5 and bmi < 25:
#         category = "Normal"
#     elif bmi >= 25 and bmi < 30:
#         category = "Overweight"
#     else:
#         category = "Obese"
    
#     return category, bmi
    
# people = int(input("Enter the number of people: "))
# for i in range(people):
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in meters: "))
#     res,bmi = calculate_bmi(weight, height)
#     print(f"Your BMI is {bmi} and {res}")

from random import *

guess = int(input("Enter a number between 1 and 10: "))
random_number = randint(1,10)

while guess != random_number:
    
    x = random_number
    tries = 1
    while x != guess:
        if guess < x:
            print("Too low!")
            tries += 1
        elif guess > x:
            print("Too high!")
            tries += 1
        guess = int(input("Enter a number between 1 and 10: "))        
    print(f"Congratulations! You guessed the number in {tries} tries!")