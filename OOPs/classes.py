# class Animal:
#     def __init__(self, name , pet , sound):
#         self.name = name
#         self.pet = pet
#         self.sound = sound
        

#     def speak(self):
#         print(f"{self.name} says {self.sound}")
        
        
#     def pet_info(self):
#         print(f"MY {self.pet} has the name {self.name} and they make the sound {self.sound}")    


# dog = Animal("champ","Dog", "Woof")

# cat = Animal("Toby","Cat","Meow")     

# dog.speak()
# cat.speak()  

# dog.pet_info()
# cat.pet_info()

# player 

# class Player:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         self.team = None
        
#     def show_stats(self):
#         print("Player Name: ", self.name)
#         print("Average points per game: ", self.score)
#         print("Team: ", self.team)
        
#     def select_team(self):
#         team = input("Enter the team name: ")
#         self.team = team 
        
# player = Player("Lebron James", 27.2)
# player.show_stats()        
 
# player.select_team()
# player.show_stats()                

# Shape 

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def show_info(self):
        print("Length: ", self.length, "cm")
        print("Width: ", self.width, "cm")
        print("Area: ", self.area(), "cm^2")
        print("Perimeter: ", self.perimeter(), "cm")
        
    def update(self ,length):
        self.updated = (self.length - length)* self.width  
        return self.updated   
    
a = int(input("Enter the length of the rectangle in cm : "))
b = int(input("Enter the width of the rectangle in cm: "))

rect  = Rectangle(a,b)
rect.show_info()

c = int(input("Enter the new length of the rectangle in cm: "))  
print("Updated Area: ", rect.update(c)) 