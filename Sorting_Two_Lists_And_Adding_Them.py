list_1 = []
list_2 = []


num_1 = int(input("ENTER THE LENGTH OF THE FIRST LIST: "))
for i in range(num_1):
    l_1 = int(input("ENTER THE NEXT NUMBER: "))
    list_1.append(l_1)
print("FIRST LIST:", list_1)


num_2 = int(input("ENTER THE LENGTH OF THE SECOND LIST: "))
for i in range(num_2):
    l_2 = int(input("ENTER THE NEXT NUMBER: "))
    list_2.append(l_2)
print("SECOND LIST:", list_2)


new_list = list_1 + list_2
new_list.sort()
print("NEW LIST:", new_list)


# Making List By User Out Put.
num_list = []
num = int(input("Enter the length of the list: "))
for i in range(num):
    nums = int(input("Enter the number for adding in list: "))
    num_list.append(nums)
print(num_list)


# Sorting The List
for j in range(len(num_list)):
    for k in range(j, len(num_list)):

        if num_list[j] >= num_list[k]:
            num_list[j], num_list[k] = num_list[k], num_list[j]

print(num_list)


# Deleting The Duplicates Numbers.
new_list = list(set(num_list))
print(new_list)
