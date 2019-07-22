#so=int(input("nhap so"))
# if so < 0:
#     print("gia_tri_tuyet_doi",-so)
#     print(so)
# else :
#     print("gia_tri_tuyet_doi",so)
nam_sinh=int(input("nhap nam sinh"))
nam_sinh=2019-nam_sinh
if nam_sinh<10:
    print("tre con")
    exit()
elif 18<nam_sinh and nam_sinh>10:
    print("thanh nien")
else:
    print("nguoi lon")

