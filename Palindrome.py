# Int Palindrome
"""
print("Let's do palindrome [:-)")
num = int(input("Enter the number: "))
New_num = num
rev = 0

while num > 0:
    last_num = num % 10
    num = num//10
    rev = rev * 10 + last_num

print(rev)

if New_num == rev:
    print("IT IS A PALINDROME:)")
else:
    print("IT IS NOT A PALINDROME [;-|")


# Str Palindrome.
name = input("Enter The Word: ")
Rname = name[::-1]
print(Rname)

if name == Rname:
    print("IT IS A PALINDROME:)")
else:
    print("IT IS NOT A PALINDROME [;-|")
"""
num = int(input("Enter the number: "))

s_num = str(num)
r_num = int(s_num[::-1])

if num == r_num:
    print(True)

else:
    print(False)
