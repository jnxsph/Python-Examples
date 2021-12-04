# defining or declaring a function
def brush_teeth():
    print("Take the toothbrush.")
    print("Put toothpaste on the toothbrush.")
    print("Clean teeth")
    print("Wash the toothbrush.")
    print("Rinse mouth.")
    
    
brush_teeth()

############################################################################

# providing information to a function
# defining the parameter
def five_times(num):
    print(num*5)


# using the parameter
five_times(7)
five_times(3)

x = 18
five_times(x)

############################################################################

# defining the parameter
def add_10(num):
    result = num + 10
    print(result)
    
   
# using the parameter    
add_10(32)

############################################################################

# defining multiple parameter
def add_numbers(first, second):
    sum = first + second
    print(sum)


# using multiple parameter
add_numbers(10, 2)

############################################################################

# using return
def add(a, b):
    return a + b
    
    
sum = add(13, 65)
print(sum)

############################################################################

# another example of using return
def add(a, b):
    return a + b
    

x = add(6, 3)
y = add(4, 5)
z = add(x, y)
print(z)

############################################################################

# another return example
# defining odd
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
        

# even them all
def evenify(num):
    check_odd = is_odd(num)
    if check_odd == True:
        even_num = num + 1
    else:
        even_num = num
    return even_num
    

# print result
result = evenify(8)
print(result)

############################################################################

# another return example
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
        
print(is_odd(5))

############################################################################

# iterative function
# multiply all numbers from 1 to 4
def factorial(num):
    fact = 1
    while num > 1:
        fact = fact * num
        num = num - 1
    return fact
    
    
# print result    
print(factorial(4))

############################################################################

# recursive function
# factorial math function
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
        
        
print(factorial(5))

############################################################################

# number multiplied by 2 function
def doublified_list(a, b,c):
    double_nums = [a * 2, b * 2, c * 2]
    return double_nums
    
    
# print result and put result in my_list
my_list = doublified_list(4, 5, 12)
print(my_list)

############################################################################

# default parameter
def add(a, b=5):
    return a + b 
    

x = add(2, 3)
print(x)

y = add(7)
print(y)

total = add(x, y)
print(total)

############################################################################

# when not sure if about the order of the parameter(arguments)
# pass arguments by their name
def add(a, b):
    return a + b
    

x = add(a=2, b=3)
print(x)

y = add(b=7, a=11)
print(y)

total = add(b=x, a=y)
print(total)

############################################################################

# Converting kilometers to miles function
def conv_miles():
    k = float(input("Enter Kilometers: "))         # Get kilometers from user
    conv_miles = 0.621371
    miles = k * conv_miles                         # formula for kilometers to be converted to miles
    return miles

print("Miles equivalent:",conv_miles())

############################################################################
