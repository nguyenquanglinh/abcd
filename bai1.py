ban_kinh=(input("ban kinh r cua hinh tron"))
try:    
    ban_kinh=float(ban_kinh)
    so_pi=float(input("so pi"))
    print(so_pi)
    dien_tich=(ban_kinh**2)*so_pi
    print(dien_tich)
    chu_vi=ban_kinh*2*so_pi
    print(chu_vi)   
except :
    print("loi")
print(ban_kinh)
