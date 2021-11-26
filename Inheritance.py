# Inheritance example
class Phone():
    video_call = True 
    def __init__(self, brand, price, network):
        self.brand = brand
        self.price = price
        self.network = network
    def recharge(self):
        print('Eating Electricity')
        print('Electrons are yummy!')

my_phone = Phone('Apple', 8000, 'TMobile')
my_phone.recharge()

class Watch():
    def __init__(self, brand, price, has_gps):
        self.brand = brand
        self.price = price
        self.steps = 0
        self.has_gps = has_gps
    def recharge(self):
        print('Eating Electricity')
        print('Electrons are yummy!')

my_watch = Watch('Fitbit', 200, False)
my_watch.recharge()

# both phone and watch classes have recharge method and both doing the same thing
# create a common class called SmartDevice
class SmartDevice:
    def recharge(self):
        print('Eating Electricity')
        print('Electrons are yummy!')

# passing the SmartDevice class to the Phone class
class Phone(SmartDevice):
    video_call = True 
    def __init__(self, brand, price, network):
        self.brand = brand
        self.price = price
        self.network = network
        
my_phone = Phone('Apple', 8000, 'TMobile')
my_phone.recharge()

# both Phone and Watch has a brand and a price attribute
# these can be entered in the SmartDevice class and call that class instead of repeating codes
class SmartDevice:
    def __init__(self, brand, price):
        self.brand = brand
        self.prince = price
    def recharge(self):
        print('Eating Electricity')
        print('Electrons are yummy!')    

class Watch(SmartDevice):
    def __init__(self, brand, price, has_gps):
        SmartDevice.__init__(self, brand, price)
        self.setps = 0
        self.has_gps = has_gps

my_watch = Watch('Fitbit', 200, False)
print(my_watch.brand)
my_watch.recharge()
