n=int(input("nhap n "))
if n < 2:
    print("khong la snt")
elif n == 2:
    print(" la so nt")
elif n %2 == 0:
    print("khong la snt")
elif n>=3:
    for i in range(3, n, 2):
        if(n %i == 0):
            print("k la snt")

# # from turtle import*
# # shape("turtle")
# # for i in range (3):
# #     forward(200)
# #     left(90)
# #     forward(200)
# #     left(90)
# #     forward(200)
# #     left(90)
# #     forward(200)
# #     left(90)
# # mainloop()
# # # bai tap ve 9 hinh tron
# from turtle import*
# import math
# x = 9
# x = math.sqrt(x)

# shape("turtle")
# for i in range(9):
#     for i in range(36):
#         forward(10)
#         right(10)
#     right(40)
