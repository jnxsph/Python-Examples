# using for loop
basket = ["Apple", "Orange", "Banana", "Strawberry"]

for fruit in basket:
    print(fruit)

#############################################################################################    

# adding multiple lines inside the for loop
basket = ["Apple", "Orange", "Banana", "Strawberry"]
for fruit in basket:
    message = "Fresh " + fruit
    print(message)

#############################################################################################
    
# for loop using numbers
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

#############################################################################################
    
# condition inside a for loop
nums = [12, 34, 65, -86, 78]
for num in nums:
    if num > 0:
        print(num)

#############################################################################################
        
# breaking a loop
nums = [12, 34, 65, -86, 78]
for num in nums:
    if num < 0:
        break
    print(num)

#############################################################################################
    
# breaking a loop in string
heroes = ['Ironman', 'Spiderman', 'Captain America', 'Thanos', 'Wanda']
for hero in heroes:
    if hero == 'Spiderman':
        break
    print(hero)

#############################################################################################
    
# skipping iteration/elements
nums = [12, 34, 65, -86, 78, 675, -67, -98, 564]
# skipping even numbers
for num in nums:
    if num % 2 == 0:
        continue
    print(num)

#############################################################################################
    
# skipping iteration/elements
nums = [12, 34, 65, -86, 78, 675, -67, -98, 564]
# skipping negative numbers
for num in nums:
    if num < 0:
        continue
    print(num)
