from module_bmi import calculate_bmi


people = int(input("Enter the number of people: "))
for i in range(people):
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    res,bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} and {res}")