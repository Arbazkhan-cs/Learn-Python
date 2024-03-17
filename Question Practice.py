'''num_1 = int(input("ENTER FIRST NUMBER: "))
num_2 = int(input("ENTER SECOND NUMBER: "))
if num_1*num_2 >= 1000:
    print(num_1+num_2)
else:
    print(num_1*num_2)


print("PRINTING CURRENT AND PREVIOUS NUMBERS AND THEIR SUM: ")
previous_number = 0
num = int(input("ENTER A NUMBER: "))
for i in range(1,num):
    sum = previous_number+ i
    print("CURRENT NUMBER ", i, "PREVIOUS NUMBER ", previous_number, "SUM: ", sum)
    previous_number =  i


name = input("ENTER YOUR NAME: ")
x_name = len(name)
for i in range(1,x_name-1,2):
    print(i,name[i])




name = input("ENTER NAME: ")
num = int(input("ENTER NUMBER: "))
x_num = name[num:]
print(x_num)




def num(num_list):
    number_x = num_list[0]
    number_y = num_list[-1]
    if number_x ==number_y:
        print("RESULT IS TRUE!")
    else:
        print("RESULT IS FALSE!")

    return num_list

num_1 = [11,20,30,40,50,10]
result = num(num_1)
print(result)



def num(num_list):
    print("GIVEN LIST IS: ",num_list)
    for num1 in num_list:
        if num1 % 5 ==0:
            print(num1)
    return ("great:)")

num_1 = [10,20,33,36,40]
result = num(num_1)
print(result)




str_x = "Emma is good developer. Emma is a writer"
print("Emma is ", str_x.count('Emma'),

num = int(input("ENTER NUMBER: "))
for i in range(num):
    for j in range(1,i+1):
        print(i, end = " ")
    print()


x_list = [10, 30, 35, 45, 50]
y_list = [40, 45, 60, 75, 90]
result_list = []
for num in x_list:
    if num % 2 !=0:
        result_list.append(num)
for num in y_list:
    if num % 2 == 0:
        result_list.append(num)
print("Result Is: ",result_list)

num  = int(input("ENTER A NUMBER: "))
print("GIVEN NUMBER", num)
while num > 0:
    digit = num % 10
    num = num // 10
    print(digit, end = "")'''


def num(x):

    if x <= 10000:
        print(10000*0,"= 10000 * 0%")

    if x == 10000:
        print(10000*0+10000*(10/100), "= 10000*0% + 10000*10%")

    if x >=10000:
        print((10000*0)+(10000*(10/100))+((x-20000)*(20/100)),"= 10000*0% + 10000*10% +",x-20000,"*20%")

    return x


num_1 = int(input("ENTER YOUR INCOME: "))
result = num(num_1)
print( "Income Tax Of:",result)










