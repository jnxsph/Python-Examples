# writing a while loop
count = 0
while count < 5:
    print(count)
    count = count + 1

# writing a while loop
count = 5
while count > 0:
    print(count)
    count = count - 1

# sum of all the numbers from 1 to 10
i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum)    
    
# getting the sum of even numbers from 1 to 10
i = 1
sum = 0
while i <= 10:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(sum)

# getting the sum of odd numbers from 1 to 50
i = 1
sum = 0
while i <= 50:
    if i % 2 != 0:
        sum = sum + i
    i = i + 1
print(sum)

# breaking while loop - will break when the value becomes 5
count = 0

while count < 15:
    if count == 5:
        break
    print(count)
    count += 1

# skipping even numbers in while loop
count = 0

while count <= 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
