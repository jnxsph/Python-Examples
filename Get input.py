#Get input from user
answer = input ("What is your age?")
age = int (answer)

#Conditions
if age < 5:
    print("Watch Tom and Jerry.")
elif age < 15:
    print("Read comic books.")
elif age < 21:
    print("Watch Family Movie.")
else:
    print("Do whatever you want.")
