
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
    def talks(self,words):
        print(f"{self.name} talks and said {words}")
    
    
    def eats(self,food):
        print(f"{self.name} eats {food} everyday ")
        
    def display_info(self):
        print("---------Object Info--------")
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"gender : {self.gender}")
        
person1= Person("Alice Kamau",23,"Female")
print(type(person1.name))
person1.display_info()
person1.talks("oop is very easy")
person1.eats("rice and beans for supper")
print("-----------------")

person2= Person("Jack",25,"Male")
print(type(person2.name))
person2.display_info()
person2.talks("python is hard")
person2.eats("ugali and fish for supper")