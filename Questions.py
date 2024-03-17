# Exercise


# Question_1
while True:
    num_1 = int(input("ENTER First NUMBER: "))
    num_2 = int(input("ENTER Second NUMBER: "))

    if num_1 * num_2 >= 1000:
        print(num_1 + num_2)
    else:
        print(num_1 * num_2)
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_2
while True:
    print("Printing current and previous number sum in a range(10)")
    pr_num = 0
    for i in range(1, 11):
        x_sum = pr_num + i
        print("Current Number", i, "Previous Number", pr_num, "Sum: ", x_sum)
        pr_num = i
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_3
while True:
    name = input("Enter Your Name: ")
    size = len(name)
    for i in range(0, size, 2):
        print("Index[", i, "]", name[i])
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_4
while True:
    def x_list(x, y):
        z = x[y:]
        return z


    name = input("ENTER YOUR NAME: ")
    num = int(input("ENTER THE NUMBER FROM WHICH PREVIOUS NUMBER WILL BE DELETED:  "))
    print(x_list(name, num))
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_5
while True:
    def num(number_list):
        x_list = number_list[0]
        y_list = number_list[-1]
        if x_list == y_list:
            return True
        else:
            return False


    num_1 = input("ENTER letters: ")
    result = num(num_1)
    print(result)
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_6
while True:
    num_1 = [10, 20, 23, 24, 25, 30, 45]
    print("Given List: " + str(num_1))
    print("Divisible By 5: ")
    for num in num_1:
        if num % 5 == 0:  # % This is for reminder value
            print(num)
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_7
while True:
    str_x = "Emma is good developer. Emma is a writer"
    cnt = str_x.count('Emma')
    print("Emma appear", cnt, "times")
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_8
while True:
    num = int(input("ENTER NUMBER FOR MAKING A RIGHT TRIANGLE: "))
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_9
while True:
    def numbers(list_1, list_2):
        ans_list = []
        for num in list_1:
            if num % 2 != 0:
                ans_list.append(num)

        for num in list_2:
            if num % 2 == 0:
                ans_list.append(num)

        return ans_list


    list_1 = [10, 20, 25, 30, 35]
    list_2 = [40, 45, 60, 75, 90]
    result = numbers(list_1, list_2)
    print(result)

    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_10
while True:
    num = int(input("ENTER THE NUMBER WHICH YOU WANT TO CONVERT IT'S REVERSE: "))
    while num > 0:
        digit = num % 10
        num = num // 10
        print(digit, end="")
    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): \n")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_11
while True:
    def num(x):

        if x <= 10000:
            print(10000 * 0, "= 10000 * 0%")

        elif x <= 20000:
            print(10000 * 0 + 10000 * (10 / 100), "= 10000*0% + 10000*10%")

        else:
            print((10000 * 0) + (10000 * (10 / 100)) + ((x - 20000) * (20 / 100)), "= 10000*0% + 10000*10% +",
                  x - 20000, "*20%")

        return x


    num_1 = int(input("ENTER YOUR INCOME: "))
    result = num(num_1)
    print("Income Tax Of:", result)

    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break

# Question_12
while True:
    Derivative = input("ENTER THE TRIGONOMETRIC FUNCTION WHICH YOU WANT DERIVATIVE OF IT: ")
    if Derivative == 'sin x':
        print("Cos(x)")
    elif Derivative == 'sinx':
        print("cos(x)")
    elif Derivative == 'cos x':
        print("-sin(x)")
    elif Derivative == 'cosx':
        print("-sin(x)")
    elif Derivative == 'tan x':
        print("Sec^2(x)")
    elif Derivative == 'tanx':
        print("Sec^2(x)")
    elif Derivative == 'sec x':
        print("Sec(x) * Tan(x)")
    elif Derivative == 'secx':
        print("Sec(x) * Tan(x)")
    elif Derivative == 'cot x':
        print("Cosec^2(x)")
    elif Derivative == 'cotx':
        print("- Cosec^2(x)")
    elif Derivative == 'cosec x':
        print("Cosec(x) * sec(x)")
    elif Derivative == 'cosecx':
        print("- Cosec(x) * Cot(x)")

    Again = input("DO YOU WANT TO DO IT AGAIN(Y/N): ")
    if Again == 'N':
        print("OK:)")
        break
    if Again == 'n':
        print("OK:)")
        break
