# for i in range(1,7):
#     for j in range(1,7):
#         if (i+j) == 6:
#             print('첫 번째 주사위=',i, '두 번째 주사위=', j)


# for y in range(5, 0, -1) :
#     for x in range(y) :
#         print("*", end="" )
#     print("")

# for y in range(5, 0, -1):
#     print(" "*(5-y), end="")
#     for x in range(y):
#         print("*", end="")
#     print(" ")

# count = int(input("반복횟수:"))

# divident = 4
# divisor = 1
# sum = 0

# for i in range (count):
#     sum +=(-1)**i * (divident/divisor)
#     divisor += 2
    
# print("Pi = %f" % sum)


# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed("fastest")
# for i in range(1000):
#     lenght = random.randint(1,100)
#     t.fd(lenght)
#     angle = random.randint(0,360)
#     t.right(angle)

# turtle.mainloop
# turtle.bye()



# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed("fastest")
# for i in range(1000):
#     t.fd(3+i*1/3)
#     t.left(30-i*1/11)

# turtle.mainloop
# turtle.bye()