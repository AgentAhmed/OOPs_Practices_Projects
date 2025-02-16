def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category =  "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        category = "Normal"
    elif bmi >= 25 and bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return category, bmi
    
