shaxs1 = {
   "ism":"Abdulhamid ",
   "familiya":"Cho'lpon",
   "tug_yil":"1897",
   "tug_joyi":"Andijon"
}
shaxs2 = {
   "ism":"Abdulla ",
   "familiya":"Avloniy",
   "tug_yil":"1878",
   "tug_joyi":"Toshkent"
}
shaxs3 = {
   "ism":"Abdulla ",
   "familiya":"Qodiriy",
   "tug_yil":"1894",
   "tug_joyi":"Toshkent"
}
shaxs4 = {
   "ism":"Alisher ",
   "familiya":"Navoiy",
   "tug_yil":"1441",
   "tug_joyi":"Hirot"
}

# shaxslar = [shaxs1,shaxs2,shaxs3,shaxs4]
# for shaxs in shaxslar:
#     print(f"{shaxs["ism"].title()} {shaxs["familiya"].title()} {shaxs["tug_yil"]}- yilda {shaxs["tug_joyi"].title()}da tavallud topgan.")
#2-mashq
# adabiyotlar = {
#         "Abdulhamid Cho'lpon":["Hayol","suygan choqlarda","Buzilgan o'lka","binafsha"],
#         "Abdulla Avloniy":["chin do'st","xijron so'zi","Maktab haqinda","Biz,millat"],
#         "Abdulla Qodiriy":["O'tgan kunlar","Jinlar bazmi","uloqda"],
#         "Alisher Navoiy":["Badoyi-ul-Bidoya","Oliyjanob shx va ojiz qul hikoyati","Shox Baxrom hikoyati"]
# }
# for k,v in adabiyotlar.items():
#     print(f" \n{k}ning mashhur asarlari:")
#     for book in v:
        # print(book)
#         3-mashq
# friends = {
#     "Ibrohim":["Afsungar","iztopar","Maymunlar qiroli"],
#     "Sarvar":["qasoskorlar","Birinchi qasoskor","Xatiko"],
#     "Samandar":["yigit so'zi","Titanic","Majrux"]
# }
# for k,v in friends.items():
#     print(f"\n{k}ning sevimli  kinolari:")
#     for movie in v:
#         print(movie.title())
#4-mashq
# count = {
#     "Uzbekistan":{
#         "poytaxti":"Toshkent",
#         "aholi soni":"37 MLN",
#         "pul birligi":"sum"
#     },
#     "Rossiya":{
#         "poytaxti":"Moskva",
#         "aholi soni":"144 MLN",
#         "pul birligi":"rubl"
#     },
#     "Aqsh":{
#         "poytaxti":"Washington",
#         "aholi soni":"331 MLN",
#         "pul birligi":"dollar"
#     },
#     "xitoy":{
#         "poytaxti":"Pekin",
#         "aholi soni":"1.41 MLRD",
#         "pul birligi":"yuang"
#     }
# }
# for k,v in count.items():
#     print("\n",k.title())
#     for ink,inv in v.items():
#         print(f"{k.title()}ning {ink} {inv}")        
count = {
    "Uzbekistan":{
        "poytaxti":"Toshkent",
        "aholi soni":"37 MLN",
        "pul birligi":"sum"
    },
    "Rossiya":{
        "poytaxti":"Moskva",
        "aholi soni":"144 MLN",
        "pul birligi":"rubl"
    },
    "Aqsh":{
        "poytaxti":"Washington",
        "aholi soni":"331 MLN",
        "pul birligi":"dollar"
    },
    "Xitoy":{
        "poytaxti":"Pekin",
        "aholi soni":"1.41 MLRD",
        "pul birligi":"yuang"
    }
}

count_name = input("davlat nomini kiriting:").title()
temp = 0
for key,value in count.items():
    if(key.title() == count_name):
        print(f"\n{key}")
        temp+=1
        for k,val in value.items():
            print(f"{k}:{val}")

if(temp == 0):
    print("bizda bunday davlat mavjud emas:(")
          
          
    


