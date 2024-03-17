"""# Exercise 2.3
rate = float(input("ENTER THE RATE: "))
hours = int(input("ENTER THE HOURS: "))
print(rate * hours)


# Exercise 3.1
hrs = float(input("Enter Hours: "))
rte = float(input("Enter the rate: "))
if hrs > 40:
    h_r = rte * hrs
    o_t = (hrs - 40.0) * (rte * 0.5)
    result = h_r + o_t
else:
    result = rte * hrs

print(result)


# Exercise 3.3
score = float(input("Enter Score: "))
if score <= 1.0:

    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score <= 0.6:
        print("F")

else:
    print("Error!!!")

# Exercise 4.6
def computepay(h, r):
    if h > 40:
        h_1 = h * r
        r_1 = (h-40)*(r*0.5)
        result = h_1 + r_1
    if h <= 40:
        result = h * r

    return result


hrs = float(input("Enter Hours:"))
rte = float(input("Enter Rates:"))

value = computepay(hrs, rte)
print("Pay", value)


                                             # For Loop
# Finding The Largest Number.
def m_a_x(num):
    k = None
    for i in num:
        if k is None:
            k = i
        if i > k:
            k = i
    return k


num_1 = [6, 3, 4, 32, 2, 44, 4, 7, 72, 5, 7, 8]
result = m_a_x(num_1)
print("Largest Number Is", result)


# Finding The smallest Number.
def m_i_n_i(num):
    k = None
    for i in num:
        if k is None:
            k = i
        if i < k:
            k = i
    return k


num_1 = [6, 3, 4, 32, 2, 44, 4, 7, 72, 5, 7, 8]
result = m_i_n_i(num_1)
print("Smallest Number Is", result)


# Counting The Numbers.
num = [1, 2, 4, 6, 0, 8, 5, 9]
k = 0
for i in num:
    k += 1
print("Total Number IS:", k)


# Summing The Lists Numbers.
def Sum(nums):
    k = 0
    for i in nums:
        k = k + i
    return k


nums = [1, 2, 3, 9, 4, 2, 8, 7]
result = Sum(nums)
print("Summation Is:", result)


def Avg(num):
    Sub = 0
    Sum = 0
    for i in num:
        Sum = Sum + i
        Sub += 1
    return Sum/Sub


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = Avg(nums)
print("Average Is:", result)


# Exercise 5.2
largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        nums = int(num)
    except:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = nums
    if nums < smallest:
        smallest = nums
    if largest is None:
        largest = nums
    if nums > largest:
        largest = nums

print("Maximum is", largest)
print("Minimum is", smallest)"""


fname = open('file.txt', 'w')











