from array import *
"""print(num)
value = int(input("ENTER THE VALUE: "))
for i in range(value):
    if value in num:
        print("INDEX NO: ", i)
print(i)"""

# It Is Not Working Properly.
"""
print("HELLO WORLD :)")

num = array('i', [])
for i in range(1, 10):
    num.append(i)

print(num)
value = int(input("ENTER THE NUMBER OF WHICH YOU WANT IT'S INDEX NO.: "))

low = 0
high = len(num)+1
while low <= high:
    mid = int((high+low)/2)

    if num[mid] == value:
        print(mid)
        break

    if value <= num[mid]:
        high = (mid+1)/2

    if value >= num[mid]:
        low = mid+1"""


# Binary Search
num = array('i', [])
num_range = int(input("ENTER THE LENGTH OF THE ARRAY: "))
for i in range(1, num_range):
    num.append(i)

print(num)
value = int(input("ENTER THE NUMBER: "))

low = 0
high = len(num) + 1
count = 1

while low <= high:
    mid = int((high + low) / 2)

    try:
        if num[mid] == value:
            print("Index NO:", mid)
            break
    except IndexError as i:
        print("The Number You Entered Is Not In The Array List [;(", "\nError Is:", i)
        quit()

    if num[mid] < value:
        low = mid

    elif num[mid] > value:
        high = mid

    print(count, ").", mid)
    count += 1
