from uuid import uuid4
class Shaxs :
    __shaxslar_soni = 0
    def __init__(self,ism,familiya,tyil,manzil,tel_raqam,email):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__manzil = manzil
        self.__tel_raqam = tel_raqam
        self.email = email
        self.__id = uuid4()
        Shaxs.__shaxslar_soni += 1

    def get_info(self):
        return f"ism:{self.ism}\nfamiliya:{self.familiya}\nt_yil:{self.tyil}\nemail:{self.email}"

    def get_id(self):
        return self.__id

    def get_location(self):
        return self.__manzil

    def get_phone(self):
        return self.__tel_raqam

    def set_phone(self,phone):
        self.__tel_raqam = phone

    @classmethod
    def get_soni(cls):
        return cls.__shaxslar_soni    


class Talaba():
    __talabalar_soni = 0
    def __init__(self,ism,familiya,tel_raqami):      
        self.__tel_raqam = tel_raqami
        self.ism =ism
        self.familiya = familiya
        Talaba.__talabalar_soni += 1
    def get_info(self):
        return f"talaba ismi:{self.ism}\n familiya:{self.familiya}"
    def get_phone(self):
        return f"phone:{self.__tel_raqam}" 
    def set_phone(self,phone):
        self.__tel_raqam = phone
    @classmethod    
    def get_soni(cls):
        return cls.__talabalar_soni    
shaxs1 = Shaxs("aliy","valiev",1999,"toshkent",945673995,"vali@gmail.com")
shaxs2 = Shaxs("aliy","valiev",1999,"toshkent",945673995,"vali@gmail.com")
shaxs3 = Shaxs("aliy","valiev",1999,"toshkent",945673995,"vali@gmail.com")
talaba1 = Talaba("shoxrux","abdullayev",956472844)
talaba1 = Talaba("shoxrux","abdullayev",956472844)
talaba1 = Talaba("shoxrux","abdullayev",956472844)
print(Talaba.get_soni())
print(Shaxs.get_soni())


        