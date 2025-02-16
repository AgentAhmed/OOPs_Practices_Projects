class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def use_hero(self):
        print(f"{self.name} is using {self.power}!")    
        
    def intro_hero(self):
        print(f"I am {self.name} and I have the power {self.power}!")
    
    
    def save_day(self):
        print(f"I am {self.name} and I am saving the day!")
        
    def power_level(self):
        length  = len(self.power)
        level = length * 10
        return level 
    
class Flying(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed
        
    def use_power(self):
        print(f"{self.name} is flying at {self.speed} mph!")
        
    def calc_distance(self, flight_time):
        distance = self.speed * flight_time
        return distance    
        
    def power_level(self):
        length  = len(self.power)
        level = length * 10
        return level + self.speed    
    
batman = Superhero("Batman", "Strength")               
batman.intro_hero()
print(batman.power_level())       

superman = Flying("Clark Kent", "Flight", 1000)
superman.intro_hero()     
superman.use_power()

flight_dist = 30
attack = superman.calc_distance(flight_dist)   
print(f"{superman.name} will attack the enemy from {attack} miles in {flight_dist} hours!")         