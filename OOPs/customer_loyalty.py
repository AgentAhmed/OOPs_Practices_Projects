class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
    
class LoyaltyPoints:
    def __init__(self):
        self.points = 0
    
    def earn_points(self, amount):
        self.points += amount
        
    def redeem_points(self, amount):
        if self.points >= amount:
           self.points -= amount        
        else:
            print("Insufficient points")
            
    def show_points_balance(self):
        print("Points balance: ", self.points)
        
class VIPcustomer(Customer, LoyaltyPoints):
    def __init__(self, customer_id, name):
        Customer.__init__(self, customer_id, name)
        LoyaltyPoints.__init__(self)
        
class Transaction:
    def __init__(self, transaction_id, customer, amount):
        self.transaction_id = transaction_id
        self.customer = customer
        self.amount = amount
        
        
class TransactionHistory:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    def show_transaction_history(self):
        for transaction in self.transactions:
            print("Transaction ID: ", transaction.transaction_id)
            print("Customer ID: ", transaction.customer.customer_id)
            print("Amount: ", transaction.amount)
            print("Customer Name: ", transaction.customer.name)
            print("Points balance: ", transaction.customer.points)
            print("\n")        
    
    
                           