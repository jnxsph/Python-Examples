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

# largest number of the 3 numbers
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3rd number: "))

largest = max(num1, num2, num3)

print("The largest number is: ", largest)

#############################################################################################

# Getting the average of number in the list using mean()
from statistics import mean
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
average = mean(numbers)
print(average)

#############################################################################################

# find second largest number
nums = [4, 5, 6, 7, 34, 54, 23, 65, 654, 76]
nums.remove(max(nums))
second_largest = max(nums)
print(second_largest)

#############################################################################################

# find second smallest number
nums = [4, 5, 6, 7, 34, 54, 23, 65, 654, 76]
nums.remove(min(nums))
second_smallest = min(nums)
print(second_smallest)

#############################################################################################

# find second smallest number using its index
nums = [4, 5, 6, 7, 34, 54, 23, 65, 654, 76]
nums = sorted(nums)
print(nums[1])

# find second smallest number using its index, second way
nums = [4, 5, 6, 7, 34, 54, 23, 65, 654, 76]
nums.sort(reverse = True)
print(nums[1])

#############################################################################################
