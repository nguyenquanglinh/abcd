while(True):
    str_=input("nhap day 2 ")
    
    if len(str_)<8 :
        print("Nhap lai pass ")
        continue
    print(str_)
    break












dayS0="1234567890"
str_=input("nhap day ")
i=0


v=0
while(True):
    if dayS0[i]==str_[v]:
        print("co so")
        break
    else:
        if len(dayS0)-1==i:
            i=0
            v+=1
        elif len(str_)-1==v:
            print("khong co")
            break
        i+=1


# n=int(input("nhap so"))
# dem=0
# while(True):
#     print("n= ",n)
#     n+=1
#     if n>=1000:
#         break