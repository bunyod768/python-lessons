import random as r

while True:
    print(
    """Son topish o'yiniga hush kelibsiz!!!
    (0-10) gacha bo'lgan son o'yladim.Topishga harakat qiling.    """
    )
    s1 = 0
    s2 = 1
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
          print(f"Siz to'g'ri topdingiz.Urunishlar soni:{s1+1} ")
          print(f"Endi siz (0 - 10) gacha bo'lgan son o'ylang . Men esa topishga harakat qilaman :)")
          input(" Boshlash uchun istalgan tugmani bosing:")
          break
      
      
    while True:
       komp_son = r.randint(0,10)
       print(f"men o'ylagan son:{komp_son}")
       yakun = input("Men o'ylagan son katta bo'sa (>),kichik bo'lsa(<) belgilardan birini qo'ying. Agar to'g'ri bo'lsa (t) harfini yozing:")
       old_son = komp_son
       if yakun == '<' or yakun == '>':         
          while True:
             s2 +=1
             if yakun == '>':
                komp1_son = r.randint(0,old_son)
                yakun = input(f"Men o'ylagan son:{komp1_son}.Katta bo'sa (>),kichik bo'lsa(<) belgilardan birini qo'ying. Agar to'g'ri bo'lsa (t) harfini yozing.")
                old_son = komp1_son
             else:
                komp1_son = r.randint(old_son,10)
                yakun = input(f"Men o'ylagan son:{komp1_son}. Katta bo'sa (>),kichik bo'lsa(<) belgilardan birini qo'ying. Agar to'g'ri bo'lsa (t) harfini yozing.")
                old_son = komp1_son
             if yakun == 't':
                print("Men o'zimni tabriklayman 😂 ")
                break
                
       if yakun == 't':         
          break
    print(f"Men {s2} marta urindim.")
    print(f"Siz esa {s1} marta urindingiz.")
    if s1 > s2:
       print("Demak siz yutqazdingiz. :(") 
    else:
       print("Tabriklayman demak siz g'alaba qozondingiz. :)")
    sorov = input("Yana o'ynaymizmi? ha(1) / yo'q(0):")
    if sorov == '0':
       break
print("O'yin yakunlandi.")              
