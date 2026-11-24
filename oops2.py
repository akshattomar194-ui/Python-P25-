#Pillars 


#Inheritance - 
# inheritance works between classes
# # there will be a parent class and a child class and the child class will inherit all the properties
# (attributes and methods ) of a parent class
 #1.Multilevel
# class Factory:
#     def __init__(self,milk ,sugar,):
#         self.milk=milk
#         self.sugar=sugar

#     def quantity (self):
#         print(f"total quantity will be {(self.milk + self.sugar)//1.5} ")


# class Factory_two(Factory):
#     def __init__(self, milk, sugar, flavour):
#         super().__init__(milk, sugar)#super ka function super class ko call karna hai
#         self.flavour=flavour
    

#     def quantity(self):
#         super().quantity()
#         print(f"Your flavour is {self.flavour}")


# akarsh=Factory(10,4)
# yash=Factory_two(20,7,"vanilla")
# akarsh.quantity()
# yash.quantity()
# yash.quantity()


 #Types of inheritance 
#2.Multilevel inheritance 
# class Animal:
#     def __init__(self,species):
#         self.species=species

#     def details(self):
#         print(f"you are a animal and your species is {self.species}")

# class Human(Animal):
#     pass

# class Robots(Human):
#     pass
# obj=Robots("dog")
# obj.details()

# class Animal :
#     a=12
#     def __init__(self,name):
#         self.name=name

#     def hello(self):
#         print("HEllo")

# class Human:
#     b=22
#     def __init__(self,age):
#         self.age=age
#     def hello(self):
#         print("Hello how are you")

# class Robot(Animal,Human):
#     def __init__(self, name,age):
#         Animal.__init__(self,name)#is jagah per animaml ke jagah super bhi use kar sakte hai but super ke case me self nhi dena padega 
#         Human.__init__(self,age)

# obj=Robot("chitti",1)
# obj.hello()
# print(obj.name)
# print(obj.age)

#3.Hybrid inheritance 
# class Animal:
#     pass

# class Human :
#     pass

# class Robot(Animal,Human):
#     pass

# class AGI(Robot):
#     pass

#4.Heirirchial inheritance
# class Animal:
#     pass
# class Human(Animal):
#     pass
# class Robot(Animal):
#     pass


#POLYMORPHISM(MEANING HAVING MANY forms or can do many tasks)
#SAME NAME MANY FORMS 
 

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        return f"Your details are {self.name} and Age is {self.age}"

class Human(Animal):
    def __init__(self, name, age,number):
        super().__init__(name, age)
        self.number=number

    def details(self):
        print(super().details())
        print(self.number)

obj=Human("HArsh",22,12345678)
obj.details()

#Method overriding happens when you are applying inheritance and in both parent and child class
#having same method name 
#so child class method overrides the parent classs method and the object 
#of child class cannot access the parent class method 

