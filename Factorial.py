# Factorial!
name = input("What Is Your Name? ")
print("Nice To See You " + name, "\U0001F970")


def multiply(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


factorial = input("Do You Want To Do Factorial:(y/n)")

if factorial == 'yes' or factorial == 'y':
    while True:
        print("Let's Do Factorial \U0001F929")

        try:
            x = int(input("Enter A Number For Factorial: "))
            print(x, "!")

            result = multiply(x)

            print(result)

        except ValueError as v:
            print("You put the wrong input!!!".upper(), "\U0001F928", "\nThe error is", v)

        again = input("Do You Want To Do It Again?\U0001F928(y/n) ")
        if again == 'yes' or again == 'y':
            continue

        elif again == 'no' or again == 'n':
            print("Ok \U0001F932")
            print("Thanks for using me \U0001F970")
            break

        else:
            print("You put the wrong input!!!".upper(), "\U0001F928")
            break

elif factorial == 'no' or factorial == 'n':
    print("Ok \U0001F932")
    print("Thanks For Using Me \U0001F970")

else:
    print("You put the wrong input!!!".upper(), "\U0001F928")
