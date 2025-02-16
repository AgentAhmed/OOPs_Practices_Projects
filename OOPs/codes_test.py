class App:
    def __init__(self , users, storage , username):
        self.users = users
        self.storage = storage
        self.username = username    
        
    def login(self):
        if self.username == "owner" and self.users >=1:
            print("Welcome ", self.username)
            print("your storage is: ", self.storage)
        else:
            print("Invalid username")  
            
    def increase_storage(self, storage):
        self.storage += storage
        print("Your storage is now: ", self.storage)
        
product_one = App(23, 100, "owner")
product_one.login()
product_one.increase_storage(100)

product_two = App(12, 120, "user")                      
product_two.login()
