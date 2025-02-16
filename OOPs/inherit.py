class Animal:
    def __init__(self, region, animal_type,color, lethal):
        self.region = region
        self.animal_type = animal_type
        self.lethal = lethal
        self.color = color
        
    def animal_bio(self):
        print("Animal Passport")
        print("Region: ", self.region)
        print("Species: ", self.animal_type)
        print("Color: ", self.color)
        print("Dangerous: ", self.lethal)    
        
class Clinic(Animal):
    def animal_info(self):
        print(f"This is a {self.animal_type} from {self.region} region")    
    
    def search(self, animals):
        region  = input("Enter region: ").lower()
        for animal in animals:
            if animal.region == region:
                print(f"Species:{animal.animal_type} ")

animals = []
amt_animals = int(input("Enter number of animals: "))   
for i in range(amt_animals):
    region = input("Enter region: ").lower()
    species = input("Enter species: ").lower()
    color = input("Enter color: ").lower()
    lethal = input("Is it dangerous? ").lower()
    lethal = lethal == "yes" 
    animals.append(Animal(region, species, color, lethal))   
    
clinic = Clinic("Africa", "Lion", "Yellow", True)  
clinic.animal_bio()
clinic.search(animals)                               