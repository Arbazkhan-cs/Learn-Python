# from turtle import *
# sc = Screen()
# sc.setup(600, 600)
# sc.bgcolor('black')
# col = ['cyan', 'indigo', 'violet', 'green', 'red', 'blue', 'yellow']
# t = 0
# speed(12000)
#
# for i in range(190):
#     # color(col[t])
#     # begin_fill()
#     color('white')
#     circle(190-i, 90)
#     left(90)
#     circle(190-i, 90)
#     right(18)
#     # end_fill()
#     if t == 6:
#         t = 0
#     else:
#         t += 1
#
# # for i in range(60):
# #     color('black')
# #     right(160)
# #     forward(i*10)
# #     if t == 6:
# #         t = 0
# #     else:
# #         t += 1
#
#
# ht()
# done()

from array import *

# count = 0
# for i in range(len(strs)):
#     x = strs[count]
#     y = strs[count+1]
#     if x[i] == y[i]:
#         print(x[i], end='')
#     i += 1

# for i in range(len(strs)):
#     print(strs[0][i])


def minimum(strs, n):
    mini = len(strs[0])
    for i in range(1, n):
        if mini > len(strs[i]):
            mini = len(strs[i])

    return mini


def common(strs, n):
    mini_len = minimum(strs, n)
    res = ""
    for i in range(mini_len):
        current = strs[0][i]

        for j in range(1, n):
            if strs[j][i] != current:
                return res

        res = res+current

    return res


strs = ["flower", "flow", "flight"]
n = len(strs)
x = common(strs, n)
print(x)
