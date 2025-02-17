# Title : Cryptocurrency management system

class Crypto:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} is a cryptocurrency'
    
    def __eq__(self, value):
        if isinstance(value, Crypto):
            return self.name == value.name
        return False
    
    def __add__(self, value):
        if isinstance(value, Crypto):
            combo = self.name + '  ' + value.name
            return Crypto(combo)
        else:
            raise ValueError('Cannot add non-crypto objects')
    
    def set_price(self , price):
        self.price += price
        
    def get_price(self):
        if hasattr(self, 'price'):
            return self.price
        else:
            print('Price not set')
    
    def calc_value(self, quantity):
        if hasattr(self, 'price'):
            return self.price * quantity
        else:
            print('Price not set')
            
class Bitcoin(Crypto):
    def __init__(self):
        super().__init__('Bitcoin')
    
    def __str__(self):
        return f"Bitcoin is decentralized"
    
    def mine(self):
        return f"Mining the next Block.."
        
class Ethereum(Crypto):
    def __init__(self):
        super().__init__('Ethereum')
    
    def __str__(self):
        return f"Ethereum is a smart contract platform"
    
    def mine(self):
        return f"Mining the next tokens.."   
    
crypto1 = Crypto('Solana') 
crypto2 = Crypto('Cardano')
crypto3 = Crypto('Bitcoin')

bitcoin = Bitcoin()
ether = Ethereum()     

# print(crypto1)

# print(bitcoin == crypto3)         

print(ether + crypto2)

ether.set_price(1750)
print(ether.get_price())   