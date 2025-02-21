class avto:
    def __init__(self,model,kompaniya,yili,rangi,narxi):
        self.model = model
        self.kompaniya = kompaniya
        self.yili = yili
        self.rangi = rangi
        self.narxi = narxi
        self.probeg = 0
    def get_info(self):
        return f""" 
        model: {self.model}
        kompaniya:{self.kompaniya}
        yili:{self.yili}
        rangi:{self.rangi}
        narxi:{self.narxi}"""
    def update_info(self,yurgan_yul):
        self.probeg += yurgan_yul
                
class Avtosalon:
    def __init__ (self,salon_nomi,manzil,tel_raqam,email):
        self.salon_nomi = salon_nomi
        self.manzil = manzil
        self.tel_raqam = tel_raqam
        self.email = email
        self.royxat = []
        self.Avtomobillar_soni = 0
        

    def Add_New_cars(self,kompaniya,model,rangi,yili,narxi):
        lugat = {
        "kompaniya":kompaniya,
        "model":model,
        "rangi": rangi,
        "yili":yili,
        "narxi":narxi}
        self.royxat.append(lugat)
        self.Avtomobillar_soni += 1
        
    def get_info_avto (self):
        return self.royxat   
    def get_info_ofise(self):
        return f"salon nomi: {self.salon_nomi}. manzil: {self.manzil}. tel raqam:{self.tel_raqam}. email:{self.email}"
avto1 = avto("Cobalt","GM",2024,"oq",9000)
print(avto1.get_info())
avto1.update_info(100)
print("yurgan masofa:",avto1.probeg)   
salon = Avtosalon("Roxat GM","Yashnobod tumani",778889988,"RoxatAvto@gmail.com")
salon.Add_New_cars("GM","kaptiva","qora",2025,10000)
salon.Add_New_cars("BMW","M5","qora",2025,30000)
avtomobilllar = salon.get_info_avto()
for x in avtomobilllar:
    print(x,"\n")
print("salondagi avtomobillar soni:",salon.Avtomobillar_soni)


            