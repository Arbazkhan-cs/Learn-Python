# Import
import math
# Name
name = input("What Is Your Name? ")
print("Nice To See You " + name)


# Define
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def percent(x, y):
    return (x/y)*100


def squ(x):
    return x*x


def square(x):
    return math.sqrt(x)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def dive(x, y):
    return x / y

# While Loop
while True:

# Select Operation
    print("1).Addition")
    print("2).Subtraction")
    print("3).Multiplication")
    print("4).Division")
    print("5).Square Root")
    print("6).Square")
    print("7).Odd And Even")
    print("8).Percentage")
    print("9).Factorial")
# Choice
    Choice = input("Select An Operation(1/2/3/4/5/6/7/8/9): ")

    if Choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter First number: "))
        num2 = float(input("Enter Second number: "))
# Addition
        if Choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
# Subtraction
        elif Choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))
# Multiplication
        elif Choice == '3':
            print(num1, "*", num2, "=", multi(num1, num2))
# Division
        elif Choice == '4':
            print(num1, "/", num2, "=", dive(num1, num2))
# SquareRoot
    elif Choice in '5':
        num3 = float(input("Enter The Number Of Which Square Root You Want: "))
        print(num3, "^", "1/2", "=", square(num3))
# Square
    elif Choice in '6':
        num4 = float(input("Enter The Number Of Which Square You Want: "))
        result = squ(num4)
        print(result)
# Odd And Even
    elif Choice in '7':
        num = float(input("Enter The Number For Finding Odd And Even: "))
        if (num % 2) == 1:
            print("Odd")
        else:
            print("Even")
# Percentage
    elif Choice in '8':
        num5 = float(input("Enter Your Total Number: "))
        num6 = float(input("Enter Your Total Marks Given From Total Number: "))
        print(num5, "*", num6, "/", 100, percent(num5, num6))
# Factorial
    elif Choice in '9':
        x = int(input("Enter A Number For Factorial: "))
        print(x, "!")
        result = factorial(x)
        print(result)
# For Invalid Input
    else:
        print("Invalid Input!!!")
# Break
    again = input("Do you want to do again(yes/no)? ")
    if again == 'no':
        print("Ok :)")
        break
# Last Line:)
print("Thanks For Using Me:)")
