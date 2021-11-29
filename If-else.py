price = 500

#if-else statement
if price < 500:
    print ("I will buy the Samsung Phone.")
else:
    print ("I will be happy with the LG.")

##################################################################################################

# Chained conditionals are simply a "chain" or a combination of multiple conditions. We can combine conditions using keywords: and, or, and not. 
# getting input from user
answer = input("What is your favorite color? ")
answer2 = input("What is your 2nd favorite color? ")

# using conditions: and, or

if answer == "Blue" and answer2 == "Black":
    print("Those colors are my favorite too!")
elif answer == "Blue" or answer2 == "Black":
    print("One of those is my favorite!")
else:
    print("Those are not my favorite. Sorry.")

##################################################################################################

# Nested Conditional is simply putting code inside of other code.
# enter 2 scores to compare
player1 = int(input("Please enter Player 1's score: "))
player2 = int(input("Please enter Player 2's score: "))

# if-else statement/ nested conditional
if player1 > player2:
    print("Player 1 WINS!")
else:    
    if player2 > player1:
        print("Player 2 WINS!")
    else:
        print("It's a Tie!")

################################################################################################## 
