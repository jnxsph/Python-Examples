# Declare Class
# create the class like a function
class Phone:
    brand = "Samsung"
  
# To see the attribute in the object created
# print the attribute by typing name of the object and then dot sign then the namen of the attribute  
my_phone = Phone()
print(my_phone.brand)

############################################################################

# Multiple Attributes
class Phone:
    brand = "Samsung"
    price = 12000
    apps = ["Programming Hero, Gmail, Facebook"]
  
new_phone = Phone()
print(new_phone.price)

############################################################################

# Declaring a method
class Phone:
    brand = "Samsung"
    
    def hard_work(self):              # just declare a function inside a class
        print("Chat, chat, chat")       # always have to provide 1 parameter. parameter is called 'self'


my_phone = Phone()
my_phone.hard_work()                # calling a method. methods are like functions


############################################################################

# Writing other parameters after the self parameter
class Calculator:
    brand = "Casio"
    def add (self, a, b):             # method name is "add". python will automatically pass the self parameter
      return a + b

calc = Calculator()
calc.add(3, 4)


############################################################################

# Storing method output to a variable and use it for other purposes
class Calculator:
    brand = "Casio"
    def deduct(self, a, b):
        return a - b


my_calc = Calculator()
result = my_calc.deduct(15, 7)
print(result)

############################################################################

# Accessing methods using the self parameter
class Bank:
    account_balance = 1000000
    def get_balance(self):               # use the self parameter to access any attributes of the class from inside a method.
        return self.account_balance

my_account = Bank()
bal = my_account.get_balance()
print(bal)

############################################################################

# Constructor method has a special name >>> __init__
# Example of a class with constructor
class Phone:
    def __init__(self, brand):           # inside the __init__ method, can just write the attribute name after the self parameter
        self.brand = brand               # Python will add that attribute to the object created by the constructor

my_phone = Phone('Samsung')
mom_phone = Phone('Nokia 3210')
print(my_phone.brand)
print(mom_phone.brand)

############################################################################

# Encapsulation example
class Bank:
    def __init__(self, name):
        self.name = name
        self.__balance = 1000000         # if an attribute has 2 underscores, it becomes private. It cannot be accessed from outside.
    def get_balance(self):               # can access the private attributes from anywhere inside the class
        return self.__balance
        
account = Bank('Daniel Chua')
print(account.name)
print(account.__balance)

############################################################################

# Polymorphism example
class Car:
    car_name = 'Toyota'                            # prints the car name and says the car is moving
    def move(self):
        print(self.car_name, 'Car is moving')
        
class Truck:
    truck_name = 'FedEx'
    def move(self):
        print(self.truck_name, 'Truck is moving')   # prints the truck name and says the truck is moving
        
class Bike:
    bike_name = 'BMX'
    def move(self):
        print(self.bike_name, 'Bike is moving')
        
        
vehicles = [Car(), Truck(), Bike()]               # list of vehicles

for vehicle in vehicles:                          # calling the move method inside the loop
    vehicle.move()                                # move method can take many forms. Based on the class it's on, it calls the right method in the right class


############################################################################
