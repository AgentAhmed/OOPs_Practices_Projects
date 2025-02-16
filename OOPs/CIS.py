# Title : Country Information System

class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.pop = population
        # self.area = area
        
    def get_info(self):
        return {
        'Name': self.name,
        'Capital': self.capital,
        'Population': self.pop,
        # 'area': self.area
         }    
        
class DevelopedCountry(Country):
    def __init__(self, name, capital, population, gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp
        
    def get_info(self):
        return {
        'Name': self.name,
        'Capital': self.capital,
        'Population': self.pop,
        'GDP': self.gdp
         }        
        
class DevelopingCountry(Country):
    def __init__(self, name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi
        
    # def get_info(self):
    #     return {
    #     'Name': self.name,
    #     'Capital': self.capital,
    #     'Population': self.pop,
    #     'HDI': self.hdi
    #      }        
    
    # we can also use super() to get the parent class method
    def get_info(self):
        info = super().get_info()   
        info['HDI'] = self.hdi
        return info
    
class World:
    def __init__(self):
        self.countries = []
        
    def add_country(self, country):
        self.countries.append(country)
        
    def get_all_countries(self):
        return self.countries
    
    def get_developed_countries(self):
        return [country for country in self.countries if isinstance(country, DevelopedCountry)]
    
    def get_developing_countries(self):
        return [country for country in self.countries if isinstance(country, DevelopingCountry)]
    
    def get_country_info(self, name):
        for country in self.countries:
            if country.name == name:
                return country.get_info()
        return None
    
    def get_country_by_capital(self, capital_name):
        for country in self.countries:
            if country.capital == capital_name:
                return country
        return None
    
    def get_country_by_population(self, population):
        for country in self.countries:
            if country.pop == population:
                return country
        return None
    
    def get_country_by_gdp(self, gdp):
        for country in self.countries:
            if country.gdp == gdp:
                return country
        return None
    
    def get_country_by_hdi(self, hdi):
        for country in self.countries:
            if country.hdi == hdi:
                return country
        return None
    
    def get_country_by_area(self, area):
        for country in self.countries:
            if country.area == area:
                return country
        return None
    
    def get_country_by_name(self, name):
        for country in self.countries:
            if country.name == name:
                return country
                
world = World()

#
usa = DevelopedCountry('USA', 'Washington DC', 328000000, 20.5) 
india = DevelopingCountry('India', 'New Delhi', 1380000000, 0.7)
china = DevelopingCountry('China', 'Beijing', 1400000000, 0.8)

world.add_country(usa)
world.add_country(india)
world.add_country(china)

#
country_info = world.get_country_info('USA')

if country_info:
    print("country_info: ")
    for key, value in country_info.items():
        print(f'{key}: {value}')                

else:
    print("Country not found")        