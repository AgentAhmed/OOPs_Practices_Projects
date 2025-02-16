# ages = [18,23,45,37]

# age  = int(input("Enter your age: "))

# while age!=0:
#     if age in ages:
#         print("You are in the list")
#     else:
#         print("You are not in the list")
#         ages.append(age)    
#     age  = int(input("Enter your age: "))

# ages.sort()
# # print("List of ages: ", ages)    

# for loops with lists 

ages = []  # Use [] instead of list()
minors = 0
seniors = 0

while True:
    age = int(input("Enter your age (0 to stop): "))  
    if age == 0:  # Exit the loop when user enters 0
        break
    
    ages.append(age)  # Append age to the list
    
    # Check age category
    if age < 18:
        minors += 1
    elif age >= 70:
        seniors += 1

print("All the ages:", ages)
print("Number of minors:", minors)
print("Number of seniors:", seniors)

# # alphabet = "A B C D E"
# # alphabet_list = alphabet.split()
# # print(alphabet_list)

# binary  = "000100001010101"
# binary_list = binary.split("1")
# print(binary_list)