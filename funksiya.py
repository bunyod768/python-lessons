#1-mashq
def sorov(ism ,yosh):
    """ foydalanuvchidan ismi va yoshini so'rab,uning tug'ilgan yilini hisoblash."""
    print(f"hurmatli {ism.title()}.Siz {yosh} yoshdasiz va {2025 - yosh}-yilda tug'ilgansiz.")

# ism = input("ismingizni kiriting:")
# yosh = int(input("yoshingizni kiriting:"))
# sorov(ism,yosh)

# 2-mashq
# son = int(input("sonni kiriting:"))
def square (son):
    print(f"{son} ning kvadrati:{son**2}\n {son} ning kubi:{son**3}")
# square(son)   
# 3-mashq
# son = int(input("Biror bir son kiriting:"))
def number(son):
    natija = ""
    if son % 2 ==0:
        natija = "juft son"
    else:
        natija = "toq son"
    print(f"{son} ",natija)
# number(son)   
#4-mashq

# son1 = int(input("1-son:"))
# son2 = int(input("2-son:"))
def solishtir(son1,son2):
    if son1 == son2:
        print("sonlar teng!")
        return
    if(son1 > son2):
        print(f"{son1} soni {son2} sonidan katta!")
    else:
        print(f"{son1} soni {son2} sonidan kichik!")
# solishtir(son1,son2)
# 5-mashq
# x = int(input("x:"))
# y = int(input("y:"))
def daraja_kotar(x,y):
    print(f"{x} ning {y} - darajasi: {x ** y}") 
# daraja_kotar(x,y)
# 6-mashq
# x = int(input("x:"))
def daraja_kotar1(x,y=2):
    print(f"{x} ning {y} - darajasi: {x ** y}") 
# daraja_kotar1(x)
    
# 7-mashq
numbeer = int(input("son:"))
boluvchilar = [2,5,7,10]
def qoldiq_hisobla(boluvchi,son):
    for bol in boluvchilar:
        if son % bol == 0:
            print(f"{son} sonimiz {bol} soniga qoldiqsiz bo'linadi.")
        else:
            print(f"{son} sonimiz {bol} soniga qoldiqsiz bo'linmaydi.")  
qoldiq_hisobla(boluvchilar,numbeer)            
