import random as r
# misol sharti: Berilgan 50ta haqiqiy sonlardan eng kattasini topadigan dastur tuzilsin.
royxat = []
# royxat yaratib 50 ta haqiqiy qiymat yuklaymiz.
for i in range(51):
   royxat.append( r.randint(-100,100))
   royxat[i] = float(royxat[i])
print(royxat)

# 1-usul
# natija = max(royxat)
# print("yechim: ", natija)

# 2- usul
maximal =  royxat[0]
for i in range(1,len(royxat)):
    if royxat[i] > maximal:
        maximal = royxat[i]
print("Maksimal element:",maximal)




