# factorial function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
  
print(factorial(4))

# Recursive factorial
def factorial(n):
    if n <= 1:                          # condition after if is the base condition(stopping condition)
        return 1
    else:
        return n * factorial(n - 1)     # calling the same factorial function

print(factorial(4))
