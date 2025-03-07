import random
# ⌈ ⌉ ⌊ ⌋ | ¯ • 
toshlar = {
    1:('⌈¯¯¯¯¯¯¯¯¯⌉',
      '|         |',
      '|    •    |',
      '|         |',
      '⌊_________⌋'),
    2:('⌈¯¯¯¯¯¯¯¯¯⌉',
      '|         |',
      '|   • •   |',
      '|         |',
      '⌊_________⌋'),
    3:('⌈¯¯¯¯¯¯¯¯¯⌉',
      '| •       |',
      '|    •    |',
      '|       • |',
      '⌊_________⌋'),
    4:('⌈¯¯¯¯¯¯¯¯¯⌉',
      '| •     • |',
      '|         |',
      '| •     • |',
      '⌊_________⌋'),
    5:('⌈¯¯¯¯¯¯¯¯¯⌉',
      '| •     • |',
      '|    •    |',
      '| •     • |',
      '⌊_________⌋'), 
    6:('⌈¯¯¯¯¯¯¯¯¯⌉',
      '| •     • |',
      '| •     • |',
      '| •     • |',
      '⌊_________⌋'),            
}

umumiy_hisob = 0
sorov = int(input("Necha marta tosh tashlamoqchisiz?(sonda)/"))
variantlar = []
for k in toshlar:
   variantlar.append(k)
tanlanmalar = []
for i in range(sorov):
    tanla = random.choice(variantlar)
    umumiy_hisob += tanla   
    tanlanmalar.append(tanla)
    # for l in toshlar.get(tanla):
    #  print(l)

for line in range(5):
    for tanlash in tanlanmalar:
        print(toshlar[tanlash][line],end=" ")
    print()    
    

print(f"Umumiy ballaringiz:{umumiy_hisob}")
    