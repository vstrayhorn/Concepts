# getInput function used for input of 2 numbers to be calculated by the user
def getInput():
    first_number = int(input("Please enter your first number: "))
    second_number = int(input("Please enter your second number: "))
    return first_number, second_number

#add function to add user input
def add():
    x, y = getInput()
    return x + y

#subtract function to add user input
def subtract():
    x, y = getInput()
    return x - y

#divide function to add user input  
def divide():
    x, y = getInput()
    return x // y

#multiply function to add user input
def multiply():
    x, y = getInput()
    return x * y

def errorHandler():
    return ("Invalid input.")

#multi-line print as options for the user 
print (
"""1. Add
2. Subtract
3. Multiply 
4. Divide
""")

#userChoice chooses an operation from the list 
userChoice = int(input("Please enter your operation choice: "))

#our operation array list
#not adding parenthesis after the function because this is not where we want to call it
#- operations = [add, subtract, divide, multiply]

#output with call the function from the operations list based on userInput
#index starts at 0 so we subtract 1 by the userChoice to get the correct index for our operations
#- output = operations[userChoice - 1]()

#print the output of the operation
#- print(output)

#our operations dictionary

operations = {
    1: add,
    2: subtract,
    3: divide,
    4: multiply
}

#since we are using indices we do not need to -1 for userChoice, we have key-value pairs
#if we are not able to process a userChoice default will be what is returned instead  
#- operations.get(userChoice, default=None)

#instead we will have a function returned if there is no userInput that can be used 
output = operations.get(userChoice, errorHandler)()

print(output)




    
    