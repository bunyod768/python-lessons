# tosh , qaychi , qog'oz
import random
variantlar = ("tosh","qaychi","qogoz")
print("Tosh ,qaychi ,qog'oz o'yiniga xush kelibsiz!")
while True:    
    
    uyinci = input("tanlang(tosh,qaychi,qogoz): ")
    if  not uyinci.isdigit():
        tanlanma = random.choice(variantlar)
        print(tanlanma)
        if tanlanma != uyinci:
            if  tanlanma == 'tosh' and uyinci == 'qogoz' or tanlanma == "qogoz" and uyinci == 'qaychi' or tanlanma == 'qaychi' and uyinci == "tosh" :
                print("Siz yutdingiz!") 
            else:
                print("Siz yutqazdingiz!")    
        else:
            print("Durrang!")        
        davom = input("Yana o'ynashni istaysizmi?(y/n)")
        if davom == 'n':
            break    
print("O'yin uchun RaxMat")   
    

