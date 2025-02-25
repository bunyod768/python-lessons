class Shaxs:
    def __init__(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.shaxs_list = []
    def __repr__(self):
        return f"Ism:{self.name}.Familiya:{self.last_name}.Yoshi:{self.age}.\n"   

class Student(Shaxs):
    __students_name = []    
    def __init__(self, name, last_name, age,lavel):
        super().__init__(name, last_name, age)
        self.lavel = lavel
        Student.__students_name.append(self.name)
    def __lt__(self,y):
        if isinstance(y,Student):
            return self.lavel < y.lavel 
    def __le__(self,y):
        if isinstance(y, Student):
            return self.age <= y.age    
    def __eq__(self,y):
        if isinstance(y,Student):
            return self.age == y.age 
    @classmethod    
    def get_names(cls):
        return  Student.__students_name
class Fan:
    __fanlar = []
    def __init__(self,name):
        self.name = name
        Fan.__fanlar.append(name)
        self.__fan_student = []
    def add_student(self,*qiymat):
        for s in qiymat:
           if isinstance(s,Student):
               self.__fan_student.append(s)
           else:
              print("obyekt notog'ri")
    def __getitem__(self,index):
        return self.__fan_student[index]
    def __len__(self):
        return len(self.__fan_student)

    def __setitem__(self,index,qiymat):
        if isinstance(qiymat,Student):
             self.__fan_student[index] = qiymat   
    def get_fan_student(self):
        return self.__fan_student
    def __add__(self,y):
        if isinstance(y , Student):
            self.add_student(y)  
    def __sub__(self,talaba):
        if isinstance(talaba,Student):
            self.__fan_student.remove(talaba) 
                   
    def __call__(self,*qiymat):
        if qiymat:
            for q in qiymat:
              if isinstance(q,Student):
               self.__fan_student.append(q)
        else:
            return self.__fan_student       
           
# student1 = Student("ali","valiyev",20,2)
# student2 = Student("hasan","husanov",20,1)
# print(student1 < student2)  
# print(student1 == student2)
# print(student1 <= student2)
# print(student1)     
# shaxs1 = Shaxs("abrot","tursunov",30)
# shaxs2 = Shaxs("tursunboy","aliyev",56)
# print(shaxs1 == shaxs2)
# print(Student.get_names())

student1 = Student("ali","valiyev",20,2)
student2 = Student("hasan","husanov",19,1)
fan1 = Fan("Matematika")
fan1.add_student(student1,student2)
new_student = Student("olim","olimov",30,1)
# fan1[1] = new_student
##print(fan1[1])
fan1 + new_student
print(fan1.get_fan_student())
print("talabalar soni:",len(fan1))
fan1 - new_student
print(fan1.get_fan_student())
print("talabalar soni:",len(fan1))
fan2 = Fan("Fizika")
fan2(student2,student1)
print(fan2.get_fan_student())
print(fan2())


