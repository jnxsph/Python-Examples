# Conversion from Miles to Kilometers

miles = float(input("Enter Distance in Miles: "))

kilometers = miles * 1.609344

print("Distance in Kilometers: ", kilometers)

#############################################################################################

# Conversion from Celcius to Fahrenheit

celcius = float(input("Enter Temperature(C): "))

fahrenheit = celcius * 9 / 5 + 32

print("Temperature(F): ", fahrenheit)

#############################################################################################

# Conversion Program

print("Temperature Conversion Program")
print("Selections:::\nPress 1 to Enter Celcius\nPress 2 to Enter Fahrenheit\nPress 3 to Enter Kelvin")

choice = int(input("Enter your Selection:"))

if choice > 3:
    print("Invalid Option")
    
    # choice number 1 Celcius to F and K
if choice == 1:
    temp = float(input("Enter Temperature(C): "))
    # Rounding to 2 decimal places
    fahrenheit = round((((9 / 5) * temp) + 32), 2)
    kelvin = round((temp + 273.15), 2)
    print('Temperature in Fahrenheit:', fahrenheit, 'deg F')
    print('Temparature in Kelvin: ', kelvin, 'deg K')

    # choice number 2 Fahrenheit to C and K
elif choice == 2:
    temp = float(input("Enter Temperature(F): "))
    celcius = round(((5 / 9) * (temp - 32)), 2)
    kelvin = round(((temp + 459.67) * (5 / 9)), 2)
    print('Temperature in Celcius:', celcius, 'deg C')
    print('Temparature in Kelvin: ', kelvin, 'deg K')

    # choice number 3 Kelvin to C and F
elif choice == 3:
    temp = float(input("Enter Temperature(K): "))
    celcius = round((temp - 273.15), 2)
    fahrenheit = round(((temp * (9 / 5)) - 459.67), 2)
    print('Temperature in Celcius:', celcius, 'deg C')
    print('Temparature in Fahrenheit: ', fahrenheit, 'deg K')

#############################################################################################

# Python program to convert decimal into other number systems
num = int(input("Enter a Decimal Number: "))

print("The decimal value of", num, "is:")
# Binary returns string since bin is a built in function of python
print(bin(num), "in Binary.") # 0b is considered binary
print(oct(num), "in Octal.") # 0o is considered octal
print(hex(num), "in Hexadecimal.") # 0x as hexadecimal

#############################################################################################





































