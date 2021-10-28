# Converting input string to in or float
num1 = int(input("Interger: "))
num2 = float(input("Float: "))

result = num1 * num2
print("Total: ", result)

#############################################################################################

# Using power
# Get input from user
num = int(input("1st number: "))
num2 = int(input("2nd number: "))

result = num2 ** num
print("Your result is: ", result)

#############################################################################################

# Using pow: python built-in function
# Get input from user
base_num = int(input("1st number: "))
power_num = int(input("2nd number: "))

result = pow(base_num, power_num)
print("Your result is: ", result)

#############################################################################################

# Using the random library
# usage of randint()
import random

random_num = random.randint(0, 10)
print(random_num)

#############################################################################################

# Floor Division: Integer part of a division
# Usage of //: getting the quotient w/o the remainder
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

result = num1 // num2
print(result)

#############################################################################################

# Usage of floor method from the math module
import math

num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

result = math.floor(num1/num2)
print(result)


#############################################################################################

# Swap two variables
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

print("1st:", num1, "2nd:", num2)

#swap them
temp = num1
num1 = num2
num2 = temp
print("1st:", num1,"2nd:", num2)

#############################################################################################

# Swap two variables
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

print("1st:", num1, "2nd:", num2)

# swap them with shortcut
num1, num2 = num2, num1
print("1st:", num1, "2nd:", num2)

#############################################################################################

# large number of 2 numbers
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

if num1 >= num2:
    largest = num1
else:
    largest = num2

print("Largest number is: ", largest)

#############################################################################################

# large number of 2 numbers
# shortcut
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

largest = max(num1, num2)

print("Largest number is: ", largest)

#############################################################################################























