import math


name = input("What Is Your Name? ")
print("Nice To See You "+name)


def gm(a, b):
    return math.sqrt(a*b)


while True:
    print("Let's Find Geometric Mean :)")
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    print(num1, "*", num2, "^", 1/2, "=", gm(num1, num2))
    again = input("Do You Want To Do It Again(y/n)? ")
    if again == 'n':
        print("OK:)")
        break
print("Thanks For Using Me:)")
