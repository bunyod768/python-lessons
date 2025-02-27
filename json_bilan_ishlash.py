import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data)
# print(data_json)

talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
# print(f"talaba ismi:{talaba_json["ism"]}\ntalaba familiyasi:{talaba_json['familiya']}")
with open("data.json",'a') as file:
    json.dump(data,file)

with open("talaba_json.json",'a') as file:
    json.dump(data,file)

with open("D:/python/python-lessons/students.json") as file:
    info = json.load(file)
num = len(info["student"])
i = 0
while i < num:
    print('name:'+info["student"][i]['name'])
    print('lastname:' + info["student"][i]['lastname'])
    print('years:' +  str(info["student"][i]['year']))
    print('faculty:'+info["student"][i]['faculty']+'\n')
    i+=1
