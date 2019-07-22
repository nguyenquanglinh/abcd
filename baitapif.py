# so=int(input("nhapso"))
# if so<0:
#     print("so am")
# else:
#     print("so duong")

# so=int(input("nhap so"))
# if so%2==0:
#     print("so chan")
# else:
#     print("so le")

# chieu_cao=int(input("nhap chieu cao"))
# can_nang=int(input("nhap can nang"))
# BMI=can_nang/(chieu_cao**2)
# if BMI<18.5:
#     print("duoi chuan")
# elif 18.5<BMI and BMI<24.9:
#     print("binh thuong")
# elif 25<BMI and BMI<29.9:
#     print("thua can")
# elif 30<BMI and BMI<34.9:
#     print("beo phi cap do I")
# elif 35<BMI and BMI<39.9:
#     print("beo phi cap do II")
# else:
#     print("beo phi cap do III")

# a=int(input("nhap do dai canh 1"))
# b=int(input("nhap do dai canh 2"))
# c=int(input("nhap do dai canh 3"))
# if a+b>c:
#     print("tam giac")
#     if a==b and a==c:
#         print("tam giac deu")
#     elif a==b or b==c or a==c:
#         print("tam giac can")
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#         print("tam giac vuong")
# else:
#     print("khong phai tam giac")

day_thon_vi_da=str("Sao,anh,không,về,chơi,thôn,Vĩ")
a=str(input("nhap chu"))
if a in day_thon_vi_da:
    print("co")
else:
    print("khong")