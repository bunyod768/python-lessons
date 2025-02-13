import math
#1-mashq
# def malumotlar(ism,familiya,ota_ismi,tel_raqam,yoshi,email=None,manzil=None):
#     malumot = {
#         "ism":ism,
#         "familiya":familiya,
#         "ota_ismi":ota_ismi,
#         "tel_raqam":tel_raqam,
#         "yoshi":yoshi,
#         "email":email,
#         "manzil":manzil
#     }
#     return malumot
# mijozlar = []
# while True:
#     ism = input("ismini kiriting:")
#     familiya = input("familiya kiriting:")
#     ota_ismi = input("ota_ismini kiriting:")
#     tel_raqam = input("tel_raqamini kiriting:")
#     yoshi = input("yoshini kiriting:")
#     email = input("email manzili:")
#     manzil = input("yashash manzili:")
#     mijozlar.append(malumotlar(ism,familiya,ota_ismi,tel_raqam,yoshi,email,manzil))
#     sorov = input("yana mijoz qo'shishni istaysizmi?(yes/no)")
#     if sorov == "no":
#         break
# print(mijozlar)
# 3-mashq
# son1 = int(input("son1:"))
# son2 = int(input("son2:"))
# son3 = int(input("son3:"))
# def findbig(son1,son2,son3):
#     numbers = [son1,son2,son3]
#     big = max(numbers)
#     return big
# katta = findbig(son1,son2,son3)
# print(f"eng katta son {katta}")
# 4-mashq
# yigish = []
# def hisobla(radius):
#     perimetr = 2 * math.pi * radius
#     diametr = perimetr / 2
#     yuza = math.pi * (radius**2)
#     doiralar = {
#         "radius":radius,
#         "perimietr":perimetr,
#         "diametr":diametr,
#         "yuza":yuza
#         }
#     return doiralar
# sorov = True
# while True:
#     if sorov:
#         radius = float(input("radiusni kiriting (sm):"))
#         yigish.append(hisobla(radius))
#         sorov1 = input("doira qo'shasizmi?(yes/no)")
#         if sorov1 =="no":
#             sorov = False      
#     else:
#         break       
# print(yigish)
#4-mashq(Oraliqdagi tub sonlar)
# Min = int(input("quyi chegara:"))
# Max = int(input("yuqori chegara:"))
# def Tub(Min=None, Max =None):
#     royxat = []
#     s = 0
#     i = 2
#     while i < Max:
#         j = 1
#         while j <= i:
#             if i % j == 0:
#                 s+=1
#             j+=1
#         if s == 2:
#             royxat.append(i)
#         s=0    
#         i+=1 
        
#     yangi_royxat = []
#     for item in royxat:
#         if item >= Min:
#             yangi_royxat.append(item)

#     return yangi_royxat 
          
# natija = Tub(Min,Max)
# print(natija)
# 5-mashq(Fibonachi ketma-ketligi)

son = int(input("hadlar sonini kiriting:"))
def fibo_hisob(son):
    fibo = [1,2]
    while len(fibo) < son:
       temp = fibo[len(fibo)-2:]
       t =sum(temp)
       fibo.append(t)
    return fibo     
natija = fibo_hisob(son)
print("Fibonachi ketma-ketligi -> \n","-> ",natija)
  




