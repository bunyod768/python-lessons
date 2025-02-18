import uzwords as uz
import random as r
def soz_ol(matn):# So'z tanlash uzwords dan
    taxmin = r.choice(matn)
    return taxmin
def find_len(text):# soz uzunligini aniqlab,uni royxat shaklida qaytarish
    uzunlik = len(text)
    soz_top = []
    for i in range(uzunlik):
        soz_top.append('-')
    return soz_top

# print(tanlanma,end=' ')
# print(tanlanma)
variantlar = []
kiritilganlar = []
while True:
    j = 0
    s = 0
    tanlanma = soz_ol(uz.words)# topiluvchi so'z
    nomalum = find_len(tanlanma) # nomalum so'z shakllandi.
    hisob = 0 # taxminlar sonini hisoblash
    tanlanma1 = set(tanlanma)
    while j != len(tanlanma1):
        for i in nomalum:           
            print(i,end=' ')
        javob = input("Belgilardan birini topishga harakat qiling:").lower()
        variantlar.append(javob)
        print("Ishlatgan belgilaringiz:",variantlar)
        hisob += 1
        for i in tanlanma:       
            if i in javob:
                nomalum[s] = tanlanma[s]                          
                j += 1              
            s += 1
        s = 0 
    variantlar = []
    print("topilgan so'z:",tanlanma)          
    print(f"Siz o'yinda {hisob} ta taxmin qildingiz.")
    yakun  = input("Yana o'ynashni hohlaysizmi?ha(1)/yo'q(0)") 
    if yakun != '1':
        break




        
        

    


    

    

     