import datetime as dt

hozir = dt.datetime.now()
# print(hozir)
bugungi_sana = hozir.date()
#print(bugungi_sana)
hozirgi_vaqt = hozir.time()
#print(hozirgi_vaqt)
# print("mcsec:",hozirgi_vaqt.microsecond)
# print("sec:",hozirgi_vaqt.second)
# print("min:",hozirgi_vaqt.minute)
# print("hour:",hozirgi_vaqt.hour)
# print("yil:",bugungi_sana.year)
# print("oy:",bugungi_sana.month)
# print("kun:",bugungi_sana.day)

ertangi_kun = dt.date(2025,3,2)
ertangi_vaqt = dt.time(12,0,0)
# oradagi farq
farq = ertangi_kun - bugungi_sana
# farqvaqt = ertangi_vaqt - hozirgi_vaqt
tug_vaqt = dt.date(2005,10,7)
yashagan_kun = bugungi_sana - tug_vaqt

#print(farq.days)
# print(f"Siz hozirgacha {yashagan_kun.days} kun hayot kechirdingiz")








