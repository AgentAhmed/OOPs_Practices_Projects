class Sport:
    def __init__(self,name):
        self.name = name 
        
    def __str__(self):
        return f"This is a {self.name} sport"
    
    def __add__(self,other):
        raise TypeError(" Not possible")
    
    def __sub__(self,other):
        raise TypeError(" Not possible")
    

class Football(Sport):
    def __init__(self,name , team):
        super().__init__(name)
        self.team = team
        
    def __str__(self):
        return f"This is a {self.name}  team and matched with teams: {','.join(self.team)}  {self.team}"   
    
    def __eq__(self, other):
        if isinstance(other, Football):
            return self.team == other.team and self.name == other.name 
        return False
    
    def __sub__(self, other):
        if isinstance(other, Football):
            shared_teams =  list(set(self.team) & set(other.team))
            if shared_teams:
                
                return Football(f"{self.name}:", shared_teams)
            else:
                return f"No common teams"
        return "Not possible"   
    
class Basketball(Sport):
    def __init__(self,name , team):
        super().__init__(name)
        self.team = team
        
    def __str__(self):
        return f"This is a {self.name}  team and matched with teams: {','.join(self.team)}  {self.team}"   
    
    def __eq__(self, other):
        if isinstance(other, Basketball):
            return self.team == other.team and self.name == other.name 
        return False
    
    def __sub__(self, other):
        if isinstance(other, Basketball):
            shared_teams =  list(set(self.team) & set(other.team))
            if shared_teams:
                
                return Basketball(f"{self.name}:", shared_teams)
            else:
                return f"No common teams"
        return "Not possible"     
    
basic = Sport("This is super basic!")

print(basic)      

football1 = Football("Football", ["Gaints", "Dolphin"])
football2 = Football("Football", ["Steelers", "Eagles"])

basketball1 = Basketball("Basketball", ["Lakers", "Celtics"])
basketball2 = Basketball("Basketball", ["jumbo", "Warriors"])

print(basic)
print(football1)
print(football2)

print(football1 == football2)
print(basketball1 == football1)

