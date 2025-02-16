class Vehicles:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        
    def get_make(self):
        if self.make == 'ford' or self.make == 'chevy' or self.make == 'tesla' :
            return "American Made"
        else:
            return "Foreign Made"
        
    def get_model(self):
        return self.model
    
    def get_year(self):
        if self.year >2000:
            return "21st century car!"
        else:
            return "This car is old...."   
        
    def get_price(self, max_price):
        if self.price < max_price:
            return "This car is cheap!"
        else:
            return "This car is expensive!"  
        
class Style(Vehicles):
    def __init__(self, make, model, year, price, num_doors):    
        super().__init__(make, model, year, price)
        self.num_doors = num_doors
        
    def get_doors(self):
        if self.num_doors == 4:
            return "This is a Family Car"
        else:
            return "This is a sports car"
        
# truck = Vehicles('ford', 'f150', 2018, 30000)
# print(truck.get_make())
# print(truck.get_price(12000))        


# car  = Style('ford', 'mustang', 2020, 9000, 2)
# print(car.get_doors())

sports_car = Style('Mahindra', 'XUV 700', 2022, 350000, 4)
print(sports_car.get_make())
print(sports_car.get_price(400000))
print(sports_car.get_doors())