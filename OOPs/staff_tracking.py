# Title: Staff Tracking System

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        
    def __str__(self):
        return f"Employee: {self.name} ({self.employee_id})" 
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id 
        return False
    
    def __add__(self,other):
        raise ValueError("Cannot add employees")
    
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
        
    def __str__(self):
        return f"Manager: {self.name} ({self.employee_id}) [{self.department}]"
    
    def __add__(self, other):
        if isinstance(other, Employee):
            return Manager(self.name, self.employee_id, self.department)
        raise ValueError("Cannot add employees")
    
    def __str__(self):
        return f"Manager: {self.name} (ID:{self.employee_id}) [Dept:{self.department}]"    
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False
    
    def __add__(self, other):
        raise ValueError("Cannot add Manager")    
    
    
class Staff(Employee):
    def __init__(self, name, employee_id, role):
        super().__init__(name, employee_id)
        self.role = role
        
        
    def __str__(self):
        return f"Name: {self.name} (ID:{self.employee_id} ,Position:{self.role}) "
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False
    
    def __add__(self, other):
        raise ValueError("Cannot add Staff")    
    
    
employee1 = Employee("John", 1001)
employee2 = Employee("Jane", 1002)

manager1 = Manager("Alice", 2001, "HR")
manager2 = Manager("Bob", 2002, "IT")

staff1 = Staff("Tom", 3001, "Engineer")
staff2 = Staff("Jerry", 3002, "Technician")    


print(employee1)
print(manager1)
print(staff1)

print(employee1 == employee2)
print(employee1 == manager1)

#print(manager1 + manager2) # adding this to check error functionality