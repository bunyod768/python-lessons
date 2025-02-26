filename = 'D:/python/python-lessons/fayllar bilan ishlash/matn.txt'
# tavsiya etilmaydi!!!
# file = open(filename)    
# rd = file.read()
# print(rd)
# file.close()

#qulay usul
# with open(filename) as file:
#     rd = file.read()
# print(rd)  
# 
# 2 - mashq
filename = 'D:/python/python-lessons/fayllar bilan ishlash/pi_million_digits.txt'  
with open(filename) as file:
    PI = file.read()
    
if '\n' in PI:  
    PI = PI.replace("\n",'')
    PI = PI.rstrip()    

print(PI)


# def found(text):
#     if text in rd:
#        return True
#     else:
#         return False
# result = found(text)
# print(result)

#3-mashq
# import pickle 
# PI = float(PI)
# with open('pkl.txt','wb') as file:
#      pickle.dump(PI,file)

#4-mashq
# msg = input("matn kiriting:")
# with open("new_file",'a') as file:
#     file.write(msg+'\n')
# print("dastur yakunlandi.")    

# import pickle
# with open("data",'wb') as file:
#     pickle.dump(PI,file)

   

