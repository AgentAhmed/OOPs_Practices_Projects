# Travel planner and cost calculator for a trip 
class Travel:
    def __init__(self, country, month, type):
        self.country = country 
        self.month = int(month)
        self.type = type
        self.price = 0
        
    def trip_info(self):
        if self.month >= 10 and self.month <= 3:
            print(f"Your trip to {self.country} in the month of Winter and this is {self.type} trip.")
        elif self.month > 3 and self.month < 10:
            print(f"Your trip to {self.country} in the month of Summer and this is {self.type} trip.")
        else:
            print("Invalid month")
            
    def calc_cost(self, cost):
        costs = []
        while cost != 0:
            self.price += cost
            costs.append(cost)
            cost = int(input("Enter cost of other expenses: "))  
            
        advice = self.advice(self.price)  
        inspect = self.list_inspect(costs)
        return advice, inspect            
    
    # call next method 
    # call checker method
    # return two things 
    
    def advice(self, num):
        if num < 500:
            print("Low budget!")
        elif num >= 500 and num < 1500:  
            print("Take a flight to anywhere..")
        else:
            print("Luxury Trip")
            
    def list_inspect(self, costs):
        less_than_ten = 0
        for i in costs:
            if i >= 10:
                less_than_ten += 1 
                
        if less_than_ten <= 10:
            self.price += 100
            print(f"Updated price: {self.price}")      

location = input("Enter the country you want to visit: ").capitalize()
type = input("Enter the type of trip Leisure or Business: ").capitalize()
month = input("Enter the month you want to visit: ")

test = Travel(location, month, type)       
test.trip_info()

flight_cost = int(input("Enter cost of flight: "))
test.calc_cost(flight_cost)

                    