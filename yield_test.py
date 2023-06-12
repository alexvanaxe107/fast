# Python program to showcase the working of yield

print("Case 0: Simple Python code for usage of yield while defining a sampleFunc()")
# Creating a user-defined function that shall calculate the various operator as seen in the function.
def mySampleFunc(x, y):
    addition = x + y
    print("The addition of the two numbers is:  ")
    yield addition
    subtract = x - y
    print("The subtraction of the two numbers is:  ")
    yield subtract
    multiply = x * y
    print("The multiplication of the two numbers is:  ")
    yield multiply
    division = x % y
    print("The division of the two numbers is:  ")
    yield division

# Calling the UDF created above and iterating the value through it in a loop using the for loop in Python.
x = 11
y = 9
print("The two numbers are: " , x, y)
print(mySampleFunc(4, 1))

print("Case 1: Simple Python code for showcasing the yield statement")
# Creating a user-defined function that shall check if the string has the letter specified inside the for loop or not.
def printOutput(string):
   for val in string:
      if val == "o":
         yield val

# Initializing the sample string as below
string = "  Hello! I am a sample string. Hope you enjoy working with the code.  "
initial = 0
print ("The number of 'o' in word is: ", end = "" )
#strip function in Python helps to remove spaces at the beginning and the end of the string.
string = string.strip()

# implmeented the for loop to iterate over the user-defined function created above-named printOutput(string)
for value in printOutput(string):
   initial = initial + 1
print (initial)

# Sample Python sample code to demonstrate yield keyword

print("Case 3: Simple Python code for usage of yield while defining a sampleFunc()")
# Creating a user-defined function that shall calculate the various operator as seen in the function.
def sampleFunc(x, y):
    addition = x + y
    print("The addition of the two numbers is:  ")
    yield addition
    subtract = x - y
    print("The subtraction of the two numbers is:  ")
    yield subtract
    multiply = x * y
    print("The multiplication of the two numbers is:  ")
    yield multiply
    division = x % y
    print("The division of the two numbers is:  ")
    yield division

# Calling the UDF created above and iterating the value through it in a loop using the for loop in Python.
x = 11
y = 9
print("The two numbers are: " , x, y)
for val in sampleFunc(x, y):
    print(val)

print("Case 4: Simple Python code for usage of yield while defining a sampleFunc()")
# Creating a user-defined function that shall calculate the various operator as seen in the function.
def sampleFuncTwo(x, y):
    addition = x + y
    print("The addition of the two numbers is:  ")
    yield addition
    subtract = x - y
    print("The subtraction of the two numbers is:  ")
    yield subtract
    multiply = x * y
    print("The multiplication of the two numbers is:  ")
    yield multiply
    division = x % y
    print("The division of the two numbers is:  ")
    yield division

# Calling the UDF created above and iterating the value through it in a loop using the for loop in Python.
# asking the users to input the first number of their choice
num1 = int(input("Please enter first number: "))
# asking the users to input the first number of their choice
num2 = int(input("Please enter second number: "))
print("The two numbers are: " , num1, num2)
for val in sampleFuncTwo(num1, num2):
    print(val)
