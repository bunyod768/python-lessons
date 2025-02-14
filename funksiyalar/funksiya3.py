# 1- mashq
# def func(names):
#     i = 0
#     while i < len(names):
#         names[i] = names[i].title()
#         i+=1
#     return names    
# ismlar = ['ali','vali','hasan','Husan']
# result = func(ismlar)
# print(result)

# 2-mashq
# ismlar = ['ali','vali','hasan','husan']

# def change(names):
#     ismlar = []
#     for name in names:
#         name = name.title()
#         ismlar.append(name)
#     return ismlar
# result = change(ismlar)
# print(result)
# print("eski natija ",ismlar)    

# 3-mashq
ismlar = ['ali','vali','hasan','husan']
def bahola(names):
    baholar = {}
    for ism in names:
        baho = int(input(f"{ism.title()}ning bahosi:"))
        baholar[ism] = baho
    return baholar
result = bahola(ismlar)
print(result)    

        

