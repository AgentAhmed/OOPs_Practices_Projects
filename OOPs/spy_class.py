from time import sleep

class Agent():
    def __init__(self, name, health, car):
        self.name = name
        self.health = health
        self.car = car
        
    def agent_info(self):
        #print(f"Agent {self.name} has {self.health} health and drives a {self.car}.")     
        print("Welcome ," , self.name)
        print("Health: ", self.health)
        print("Car: ", self.car)
        
class Spy(Agent):
    def __init__(self, name, health, car, agency , location):
        super().__init__(name, health, car)    
        self.agency = agency
        self.location = location
        self.killed = False   
        
    def assassinate(self, bad_guy):
        if bad_guy.health > 0:
            bad_guy.health -= 20
            print(f"{bad_guy.name} has been shot! Health is now {bad_guy.health}.")
            if bad_guy.health <= 0:
                self.killed = True
                print(f"{bad_guy.name} has been killed. {self.killed} is now on the run.")
              
        
# james_bond = Agent("James Bond", 100, "Aston Martin")
# ethan_Hunt = Agent("Ethan Hunt", 100, "BMW")

james_bond = Spy("James Bond", 100, "Aston Martin", "MI6", "London")
ethan_Hunt = Spy("Ethan Hunt", 100, "BMW", "IMF", "Washington D.C.")

james_bond.agent_info()
ethan_Hunt.agent_info()  
sleep(5)    

while ethan_Hunt.health > 0:
    james_bond.assassinate(ethan_Hunt)  
    ethan_Hunt.assassinate(james_bond)
    sleep(2)