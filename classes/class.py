class User:
     def __init__ (self,ism,familiya,yosh):
         self.ism = ism
         self.familiya = familiya
         self.yosh = yosh
     def get_info(self):
         return f"hello my name is {self.ism}\nMy lastname is {self.familiya}\nmy age is {self.yosh}"
foydalanuvchi = User("Bunyod","Abduvaitov",20)
print(foydalanuvchi.get_info())
        


