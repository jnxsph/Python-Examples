# Get input from user
answer = input("Year: ")
year = int(answer)

# Condition for leap year/ divisible by 4 = Leap Year
if year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
    
#############################################################################################

# Get input from user
answer = input("Who are you? ")
words = answer


# Condition for words since they can be recognized by the space after it
count = 0
for words in answer:
    if words == ' ':
        count = count + 1

# add one for the last word
count = count + 1

print(count)

#############################################################################################

# Get input from user
answer = input("Say Something: ")
sentence = answer

# define counting of vowels in a sentence


def vowels(sentence):
    count = 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in sentence:
        if char in vowels:
            count += 1
    return count
  
#############################################################################################    

# print the number of vowels
print(vowels(answer))

# remove duplicates
def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique
    
    
number = [1, 2, 2, 4, 5, 6, 7, 3, 4, 5, 6, 7, 8, 9, 0, 21, 321, 32, 43, 54, 64, 23, 32, 21, 43]
print(remove_duplicates(number))

#############################################################################################

# Fibonacci Series
# definition of loop
def fibonacci(num):
#starting with first 2 numbers
    fibo = [0, 1]
#started with the 3rd number
    i = 2
# loop for the sum of the next numbers
    while i <= num:
        next_fibo = fibo[i - 1] + fibo[i - 2]
        fibo.append(next_fibo)
        i += 1
    return fibo
    

# fibonacci until number 9    
print(fibonacci(9))

#############################################################################################

# Merge and Sort Array Function
def merge(first, second):
    combined = first + second
    combined.sort()
    return combined
    
    
# call the merge function
group1 = [11, 13, 15, 17, 19]
group2 = [10, 12, 14, 16, 20]
merged = merge(group1, group2)
print(merged)

#############################################################################################

# Define Multiplication table
def multp_table(n):
    i = 1
    while i <= 10:
        print(i, "X", n, "=", i*n)
        i += 1


multp_table(9)
