 
# class Talaba():
#     def __init__ (self,ism,familiya,tyil):       
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil 
#         self.fanlar = []       
#     def fanga_yozil(self,nomi):
#         self.fanlar.append(nomi)
#         self.nomi = nomi
#     def get_fanlar(self):
#         return [x.fan_info() for x in self.fanlar]
#     def fan_info(self):
#         return f"fan nomi:{self.nomi}" 
#     def remove_fan(self,dalate):
#         self.dalate =dalate 
#         if dalate in self.fanlar:
#             self.fanlar.remove(dalate) 
#             return
#         else:print("siz bu fanga yozilmagansiz!!!")  

# class Fan(Talaba):
#     def __init__(self,nomi):
#         self.nomi = nomi        
#     def fan_info(self):
#         return f"fan nomi:{self.nomi}"    
#     def get_info(self):
#         return [x.fan_info() for x in self.fanlar] 
    
    
# matem = Fan("matem")
# fizika  = Fan("fizika")
# english = Fan("english")
# talaba1 = Talaba("Ibrohim","shodmonov",2017)
# talaba2 = Talaba("Hasan","Husanov",1997)
# talaba1.fanga_yozil(matem)
# talaba1.fanga_yozil(fizika)
# talaba2.fanga_yozil(english)
# talaba1.remove_fan(fizika)
# print("birinchi talaba:",talaba1.get_fanlar())
# print("ikkinchi talaba:",talaba2.get_fanlar())

class Shaxs:
    def __init__(self, ism, familiya, tyil, pasport):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.pasport = pasport

    def get_ism(self):
        return self.ism

    def get_familiya(self):
        return self.familiya

    def get_tyil(self):
        return self.tyil

    def get_pasport(self):
        return self.pasport

    def get_info(self):
        return f"Ism: {self.ism}. Familiya: {self.familiya}. Tug'ilgan yil: {self.tyil}. Passport raqami: {self.pasport}"


class Professor(Shaxs):
    def __init__(self, ism, familiya, tyil, pasport, ilmiy_daraja):
        super().__init__(ism, familiya, tyil, pasport)
        self.ilmiy_daraja = ilmiy_daraja

    def get_info_ilm(self):
        return f"Ilmiy darajasi: {self.ilmiy_daraja}"

    def get_info(self):
        return f"Ism: {self.ism}. Familiya: {self.familiya}. Tug'ilgan yil: {self.tyil}. Passport raqami: {self.pasport}. Ilmiy daraja: {self.ilmiy_daraja}"


class Haydovchi(Shaxs):
    def __init__(self, ism, familiya, tyil, pasport, guvohnoma_raqami):
        super().__init__(ism, familiya, tyil, pasport)
        self.guvohnoma_raqami = guvohnoma_raqami

    def get_info_guvohnoma(self):
        return f"Guvohnoma raqami: {self.guvohnoma_raqami}"

    def get_info(self):
        return f"Ism: {self.ism}. Familiya: {self.familiya}. Tug'ilgan yil: {self.tyil}. Passport raqami: {self.pasport}. Guvohnoma raqami: {self.guvohnoma_raqami}"


class Imtihon_topshiruvchi(Haydovchi):
    def __init__(self, ism, familiya, tyil, pasport, guvohnoma_raqami, malumoti):
        super().__init__(ism, familiya, tyil, pasport, guvohnoma_raqami)
        self.malumoti = malumoti

    def get_info_uquvchi(self):
        return f"Malumoti: {self.malumoti}"


shaxs1 = Shaxs("Obid", "Obidov", 2000, "AC0712342")
professor1 = Professor("Shavkat", "Madraximov", 1969, "AD0832681", "Professor")
haydovchi1 = Haydovchi("Zohid", "Kurbanov", 1968, "AC3466272", 12345678)
talaba1 = Imtihon_topshiruvchi("Jahongir", "Aliev", 2005, "AD4673992", 98765432, "O'rta")

print(shaxs1.get_info())
print(professor1.get_info()) 
print(haydovchi1.get_info())
print(talaba1.get_info())

   