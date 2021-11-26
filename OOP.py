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
