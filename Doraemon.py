# Doraemon with Python Turtle
from turtle import *
sc = Screen()
sc.setup(630, 630)
speed(9)
pensize(3)
# bgcolor("black")
# color('cyan')


def angle(x, y):
    penup()
    goto(x, y)
    pendown()


def face_circle():
    fillcolor("#ffffff")  # Eye color
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()


def mustache():
    angle(-32, 135)
    seth(165)
    fd(60)

    angle(-32, 125)
    seth(180)
    fd(60)

    angle(-32, 115)
    seth(193)
    fd(60)

    angle(37, 135)
    seth(15)
    fd(60)

    angle(37, 125)
    seth(0)
    fd(60)

    angle(37, 115)
    seth(-13)
    fd(60)


def smile():
    angle(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


def leash():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


def nose():
    angle(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def left_eye():
    # For Left Eye
    seth(0)
    angle(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    # For Right Eye
    pensize(6)
    angle(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    # White Dote In Inner Left Eye
    angle(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    angle(0, 0)


def face():
    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    angle(63.56, 218.24)
    seth(90)
    face_circle()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    face_circle()
    penup()
    seth(180)
    fd(64)


def outline_face():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#03b1fc')  # Face Color
    begin_fill()
    circle(150, 280)
    end_fill()


def doraemon():
    outline_face()

    leash()

    face()

    nose()

    smile()

    mustache()


# Body

# Left Hand
    angle(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)

    fillcolor('#03b1fc')  # Body Color  #03b1fc For Blue Color
    begin_fill()
    seth(230)
    fd(80)


# For Body Line
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)

    fd(70)
    seth(100)
    circle(-1000, 9)


# Right Hand
    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    circle(-30, 230)
    seth(45)
    fd(81)

    seth(0)
    fd(203)

    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()


# Left-Hand Color
    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()


# Left Leg
    angle(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()


# Right Leg
    angle(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()


# Right-Hand Color
    angle(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()


# Pocket
    angle(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    angle(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)
    angle(-103.42, 15.09)
    fd(90)


# Bell
    seth(70)
    fillcolor('#ffd200')
    begin_fill()
    circle(-20)
    end_fill()

    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180 - 10)
    circle(100, 22)
    end_fill()

    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    penup()
    goto(24, 15)
    pendown()
    right(90)
    fd(49)
    angle(0, -150)

    left_eye()


# Complete
doraemon()
angle(-30, -270)
write('by Inaya Khan', font=("Bradley Hand ITC", -30, "bold"))

done()


# Recursion
# def fact(num):
#     if num == 1:
#         return 1
#     return num*fact(num-1)
#
#
# result = fact(5)
# print(result)


# # include<stdio.h>
# int main() {
#
#     for(int i=0, i<=10, i++){
#         printf("%d \n", i);
#     }
#     return 0;
#
# }


# # include<stdio.h>
# int main(){
#     int num;
#     printf("Enter the number: ");
#     scanf("%d", &num);
#
#     int i = 0;
#     while(i<=num) {
#         printf("%d \n", i);
#         i++;
#     }
#
#     return 0;
# }


# # include<stdio.h>
# int main() {
#     int n;
#     printf("Enter the number: ");
#     scanf("%d", &n);
#
#     int i=0
#     int sum=0
#
#     do{
#         sum = sum+i;
#         i++;
#     } while(i<=1);
#
#     printf("%d", j);
#
#     return 0;
#
# }


# # include<stdio.h>
# int main() {
#     int n;
#     printf("Enter the number: ");
#     scanf("%d", %n);
#
#     for(i=1, i<=10, i++){
#         printf("%d \n", n*i);
#     }
#     return 0;
#
# }


# # include<stdio.h>
# int main() {
#     int n;
#     printf("Enter the number: ");
#     scanf("%d", &n);
#     int sum_n=1;
#
#     for(i=1, i<=n, i++){
#         sum_n = i*sum_n;
#
#     }
#      printf("Factorial is: %d \n", sum_n);
#
#     return 0;
#
# }
