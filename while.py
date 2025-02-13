#parol = qwerty1234
# parol = input("parolni kiriting:")
# while(True):
#     if(parol == "qwerty1234"):
#         print("tizimga kirish mumkin:)")
#         break
#     parol = input("parol xato qayta kiriting:(")

#yarim uchburchak yasash
# height = int(input("Uchburchak balandligi >>"))
# i=0
# while(i <= height):
#     print("*" * i)
#     i+=1

# 1-mashq
# i=1
# while True:    
#     book = input(f"Yoqtirgan kitobim:({i}):")
#     savol=input("yana qo'shasizmi?(ha/yo'q)")
#     i+=1
#     if savol != "ha":
#         break
# print("dastur tugadi.")
# 2-mashq

# while True:
#     yosh = int(input("Yoshingizni kiriting:"))
#     if(yosh < 7):
#         chipta = 2000
#     elif yosh < 18:
#         chipta = 3000
#     elif yosh <65:
#         chipta = 30000
#     else:
#         chipta = str(chipta)
#         chipta = "bepul :)"
#     print(f"chipta narxi:{chipta}")    
#     sorov = input("yana davom ettirishni istaysizmi?(ha/yo'q)")
#     if sorov != "ha":
#         break    
# print("dasteu tugadi!")   
# 3-mashq
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat < 0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

#while in lists
# 1-mashq
# savol = "Buyurtma berishingiz mumkin:)"
# i = 1
# buyurtmalar = []
# while True:
#     sorov = input(savol+f" {i}.")
#     buyurtmalar.append(sorov.title())
#     sorov2 = input("yana qo'shishni hohlaysizmi?(ha/yo'q)")
#     i+=1
#     if sorov2 != "ha":
#         break

# print("\n Buyurtmalaringiz:")
# for buyur in buyurtmalar:
#     print(buyur)

#2-mashq
# print("Maxsulotlarni kiritish dasturiga xush kelibsiz! ")
# e_bozor = {}
# savol = "elementlar qoshish:"
# satr = ""
# savol2 = "narxni kiritish:"
# narx = ""
# i = 1
# while True:
#     satr  = input(savol+f" {i}.")
#     narx = input(savol2 + f" {i}.")
#     e_bozor[satr] = narx
#     i+=1
#     end = input("yana maxsulot qo'shasizmi?(ha/yo'q)")
#     if end != "ha":
#         break
# print("kiritilgan maxsulotlar:")
# for k,v in e_bozor.items():
#     print(f"{k} maxsulotimiz : {v} narxda")

#3-mashq
buyurtmalar = ["olma","anjir","shaftoli","behi"]
maxsulotlar = {
    "olma":10000,
    "shaftoli":30000,
    "behi":50000,
    "anor":45000
}

while buyurtmalar:
    for buyur in buyurtmalar:
        if buyur in maxsulotlar:
            print(f"{buyur} narxi {maxsulotlar[buyur]}")
            buyurtmalar.remove(buyur)
        else:
            print(f"Bizda {buyur} maxsuloti yo'q!")
            buyurtmalar.remove(buyur)
print("dastur yakunlandi.")





    
     


  


        