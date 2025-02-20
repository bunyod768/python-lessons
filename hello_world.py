
sonlar = list(map(lambda x : x ** 2,[1,2,3,4,5,6,7,8,9,10]))
print("darajaga oshirish")
print(sonlar)
def func(son):
    if(son > 0):
        return son
print("filterlangan sonlar")    
numbers = list(filter(func,[-1,-3,2,5,-4,9]))
print(numbers)
import random
num = random.randint(0,9)

print("tavakkal son:",num)
royxat = ["salom","xayr","Ibrohim","do'stlar","vatan","maktab","talaba","vaqt"]

soz = random.choice(royxat)
print("tanlangan so'z:", soz)

sozlar = random.sample(royxat,3)
print(sozlar)
    


   
    