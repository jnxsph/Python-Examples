# Swap variable
# use a temp variable to swap two variables
first = 'Beyonce'
second = 'Kim Kardashian'
print(first, second)

temp = first              # declaring a temporary variable
first = second            # puttting the value of the first variable to the temp.
second = temp             # setting the value of the second variable to the first
print(first, second)

###################################################################################################################

# range is a function used to provide a range of numbers
# numbers from 0 to 5 will be shown
for i in range(5):
    print(i)
    
###################################################################################################################

# if you want the range to start from another number other than 0
# pass two parameters to the range function
for i in range(5, 9):
    print(i)

###################################################################################################################
