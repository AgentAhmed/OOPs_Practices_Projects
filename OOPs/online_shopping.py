# Title : Online Shopping System

class User:
    def __init__(self, username , email):
        self.username = username
        self.email = email
        
class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.cart = []
        
    def add_to_cart(self, product):
        self.cart.append(product)
        
    def remove_from_cart(self, product):
        self.cart.remove(product)
    
    def view_cart(self):
        print("Items in cart: ")
        for product in self.cart:
            print(product.name)
        
    # def get_cart(self):
    #     return self.cart     
    
    # filename.txt
    def save_cart(self, filename):
        with open(filename, "w") as file:
            file.write("Customer Cart:\n")  # Header
            file.write("=" * 20 + "\n")  # Separator
            for product in self.cart:
                file.write(f"Product: {product.name} | Price: ${product.price}\n")  # Better readability
        print(f"Cart saved to {filename}")
        
class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def remove_product(self, product):
        self.products.remove(product)
        
    def view_products(self):
        print("Products: ")
        for product in self.products:
            print(product.name)      
            
    def save_products(self, filename):
        with open(filename, "w") as file:
            file.write("Seller Product List:\n")  # Header
            file.write("=" * 30 + "\n")  # Separator
            for product in self.products:
                file.write(f"Product: {product.name} | Price: ${product.price}\n")  # Formatting
        print(f"Products saved to {filename}")
        
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def basic_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

customer = Customer("Alice", "alice@yahoo.com")
seller = Seller("Bob", "bob@gmail.com")

product1 = Product("Laptop", 1000)
product2 = Product("Mobile", 500)      
product3 = Product("Tablet", 300)
product4 = Product("Headphones", 50)    

customer.add_to_cart(product1)
customer.add_to_cart(product2)
customer.add_to_cart(product3)
customer.add_to_cart(product4)

customer.view_cart()  

customer.save_cart("cart.txt")

customer.remove_from_cart(product2)

customer.view_cart()


#
seller.add_product(product1)
seller.add_product(product2)
seller.add_product(product3)

seller.view_products()

seller.save_products("products.txt")    
                          