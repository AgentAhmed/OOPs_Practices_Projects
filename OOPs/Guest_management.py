# Title : Guest Management and Loyalty Program

class Guest:
    def __init__(self, first,last, rank, age):
        self.last_name = last
        self.first_name = first
        self.rank = int(rank)
        self.age = int(age)
        
    def guest_info(self, all_guests):
        for guest in all_guests:
            print(guest.first_name, guest.last_name, "Age", guest.age)
            
    def loyalty_program(self, all_guests):
        # Gold Member >= 10
        
        # 1. Create a list for any guest who meets certain condition
        # 2. For every guest in my list , add their last name to the list 
        # 3. 
        
        gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
        
        if gold_members:
            print("Gold Member")
            for member in gold_members:
                print("\tGuest:", member)   
                
    def guest_avg(self , all_guests):
        total_avg = 0
        for guest in all_guests:
            total_avg += guest.age
        
        avg_age = total_avg / len(all_guests)
        print("Average Customer Age:", avg_age)  
        

all_guests = list()
num_guests = int(input("Enter the number of guests: "))
for i in range(num_guests):
    data = input("Enter the guest's last name, first name, rank, and age: ").split("/")
    # data = ["John","Doe","1","25"]
    guest = Guest(data[0], data[1], int(data[2]), int(data[3]))
    all_guests.append(guest)
    
guest = all_guests[0] 
guest.loyalty_program(all_guests)   
guest.guest_avg(all_guests)
guest.guest_info(all_guests)
                              
        