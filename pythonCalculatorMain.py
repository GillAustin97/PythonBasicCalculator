
#import functions from other files
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


#prints welcome message to the user
print("Welcome to the Python Calculator!")
print("---------------------------------")

def calculator():

    #prints the operation choices to the user
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    #prompts user to choose an operation
    choice = input("Enter choice: ")

    #after user chooses operation, it prompts the user to enter two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        #using f string format to print the results of addition. 
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        #using f string format to print the results of subtraction.
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        #using f string format to print the results of multiplication.
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        #using f string format to print the results of division.
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    else:
        print("Invalid input") #if user inputs invalid operation choice, it prints "Invalid input"



#defines if __name__ == "__main__" to run the calculator function when the script is executed directly
if __name__ == "__main__":
    calculator()