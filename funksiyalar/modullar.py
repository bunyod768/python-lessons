import funksiya2 as f

# son = int(input("fibonachi ketma-ketligining hadlari sonini kiriting:"))

# result = f.fibo_hisob(son)
# print(result)

# MIN = int(input("tub sonlar ketma-ketligining quyi chegarasini kiriting:"))
# MAX = int(input("tub sonlar ketma-ketligining yuqori chegarasini kiriting:"))
# result = f.Tub(MIN,MAX)
# print(result)

import random as r
# oraliqdagi sonlarni random qilish
# son = r.randint(0,100)
# print(son)

# listdan elementlarni tanlab olish
# friends = ['sarvar','ibrohim','samandar','otabek','shoxruh','nurmuhammad','shohjahon','bexruz']

# tanla = r.choice(friends)
# print(f"tanlangan do'st: {tanla}")
# print(friends)

# qadamli ketma-ketlikdan element tanlash
# x = list(range(1,41,4))
# print(r.choice(x))
# print(x)

#shuffle (royxatni aralashtirish)

# x = list(range(1,16))
# print(x)
# r.shuffle(x)
# print(x)

# uzunlik = lambda x : x*x
# print(uzunlik(2))

# uzunlik = lambda x , y : x + y
# print(uzunlik(2,3))

# def daraja(n):
#     return lambda x : x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print("kvadrat:",kvadrat(4))
# print("kub:",kub(7))
royxat = list(range(0,11))
i = r.choice(royxat)
royxat.remove(i)
print(i)
print(royxat)





 