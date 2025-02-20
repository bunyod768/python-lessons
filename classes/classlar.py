class Foydalanuvchi:
    def __init__ (self,ism,familiya,tug_yili,login,parol,email):
        self.ism = ism
        self.familiya = familiya
        self.tug_yili = tug_yili
        self.login = login
        self.parol = parol
        self.email = email
    def get_info(self):
        return f""" foydalanuvchi:
        ismi:{self.ism}
        familiyasi:{self.familiya}
        tug'ilgan yili:{self.tug_yili}
        login:{self.login}
        parol:{self.parol}
        email:{self.email}"""    

user = Foydalanuvchi("Bunyod","Abduvaitov",2005,"Bunyodbek","Uzbekman","b8515574@gmail.com")
result = user.get_info()
print(result)
print(user)