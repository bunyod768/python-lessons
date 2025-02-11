# class without constructors
# class Point:
    
#     def talk(self):
#         print("talker")
#     def listener(self):
#         print("listen")


# point1 = Point()
# point1.listener()

#with constructors

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Name (self):
        print(f"hello Mr {self.name}")
    def Age (self):
        print(f"your age {self.age} right?")        


person = Person("Bunyod",20)        
person.Name()
person.Age()
        


