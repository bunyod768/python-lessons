class avto:
    def __init__(self,rangi,nomi,comp,yili,masofa = 0):
        self.rangi = rangi
        self.nomi = nomi
        self.comp = comp
        self.yili = yili
        self.masofa = masofa
    def chrang(self,new_col):
        self.rangi = new_col
    def add_masofa(self,dis):
        self.masofa += dis        
    @classmethod
    def func(self,xolati):
        print(xolati)
kobalt = avto("oq","kobalt","chevrolet",2025)
malibu = avto("qora","malibu","Chevrolet",2024)
kobalt.chrang("qora")
print(kobalt.rangi)
             
