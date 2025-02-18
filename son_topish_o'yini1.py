import random as r
def func(quyi,yuqori):
   number = r.randint(quyi,yuqori)
   return number

while True:
    print(
    """Son topish o'yiniga hush kelibsiz!!!
    (0-10) gacha bo'lgan son o'yladim.Topishga harakat qiling.    """
    )
    s1 = 0
    s2 = 0
    komp_son = r.randint(0,10)#kompyuter son o'yladi
    while True:
        gr_son = int(input("son kiriting:")) #o'yinchi soni
        if komp_son != gr_son:
          s1+=1
          if komp_son < gr_son:
             print("Xato! kichikroq son o'ylang :)")
          else:
             print("Xato! Kattaroq son o'ylang :)")
        else:
          s1 +=1
          print(f"Siz to'g'ri topdingiz.Urunishlar soni:{s1} ")
          print(f"Endi siz (0 - 10) gacha bo'lgan son o'ylang . Men esa topishga harakat qilaman :)")
          input(" Boshlash uchun istalgan tugmani bosing:")
          break
      
    yuqori = 10
    quyi = 0 
    sorov = '' 
    son1 = func(0,10)
    son0 = son1
    
    while sorov != 't':
       #1-usul
       print(f"Men {son0} sonini o'yladim.")
       s2+=1             
       sorov = input("Sizni soningiz katta bolsa,'>' kichik bolsa,'<' agar togri bolsa,'t' belgilarini qo'ying ")
       if sorov == '<' or sorov == '>':         
          if sorov == '>':
             son2 = func(son0,yuqori)
             yuqori -= 1
             print(f"Men {son2} sonini o'yladim.")
             sorov = input("Sizni soningiz katta bolsa,'>' kichik bolsa,'<' agar togri bolsa,'t' belgilarini qo'ying ")
             son0 =  son2
             s2 += 1
          else:
             son2 = func(quyi,son0)
             quyi += 1 
             print(f"Men {son2} sonini o'yladim.")
             sorov = input("Sizni soningiz katta bolsa,'>' kichik bolsa,'<' agar togri bolsa,'t' belgilarini qo'ying ")
             son0 = son2
             s2 += 1  
      #  if sorov == 't':
      #     s2 += 1
      #     print("Tabriklayman. Topdingiz")
      #     break
    print("Tabriklayman. Topdingiz")        
             
       # 2-usul
      #  komp_son = r.randint(0,10)
      #  print(f"men o'ylagan son:{komp_son}")
      #  yakun = input("Men o'ylagan son katta bo'sa (>),kichik bo'lsa(<) belgilardan birini qo'ying. Agar to'g'ri bo'lsa (t) harfini yozing:")
      #  old_son = komp_son
      #  if yakun == '<' or yakun == '>':         
      #     while True:
      #        s2 +=1
      #        if yakun == '<':
                
      #           yakun = input(f"Men o'ylagan son:{komp1_son}.Siz o'ylagan son {komp1_son} dan katta bo'sa (>),kichik bo'lsa(<) belgilardan birini qo'ying. Agar to'g'ri bo'lsa (t) harfini yozing.")
                
      #        else:
                
      #           yakun = input(f"Men o'ylagan son:{komp1_son}. Siz o'ylagan son {komp1_son} dan katta bo'sa (>),kichik bo'lsa(<) belgilardan birini qo'ying. Agar to'g'ri bo'lsa (t) harfini yozing.")
                
      #        if yakun == 't':
      #           print("Men o'zimni tabriklayman  ")
      #           break
                
      #  if yakun == 't':         
      #     break
    print(f"Men {s2} marta urindim.")
    print(f"Siz esa {s1} marta urindingiz.")
    if s1 > s2:
       print("Demak siz yutqazdingiz. :(") 
    else:
       print("Tabriklayman demak siz g'alaba qozondingiz. :)")
    if s1 ==s2:
       print("Menimcha durrang.")   
    sorov = input("Yana o'ynaymizmi? ha(1) / yo'q(0):")
    if sorov == '0':
       break
print("O'yin yakunlandi.")              
