 # class , objects 

# creating a class
# class College:
#     pass

#attributes and methods
# a variable defined inside a class is a attribute
# a function defined inside a class is a method 

# class Animal:
#     name="Lion"# attribute
#     print("How are you")
#     def speak():#method
#         print("Lion Roars")
# #here in general ye directly execute mhi hota
#  print statement if function call nhii kiya hita  but ye class me hai isliye execute hojayega

#everything inside a class is initialised only a single time that means
#  everyline inside the class is goint to get executed once

# accesing atrributes and methods
# class Student:
#     name="Harsh"
#     def details():
#         print("Hello my name is harsh")


#accesing attribute
# print(Student.name)
# #accessing method
# Student.details()



# objects 
# if we call a class inside a variable that variable becomes an object 
# class Animal():
#     name="Lion "

# obj =Animal()#here we created an object 
# print(obj.name)


# class Factory :
#     name="Puma"
#     print("Hello")
#     def details(self):
#         print("Hello this is puma factory")

# a=Factory()#here a is a object 

# #objects can also access attributes and methods defined inside the class 

# print(a.name)
#a.details()# an invissible argument is passed and is the location of the object 
# when you call any method using any object location is passed 


# a constructor function is a tyoe of dunder method that will be automatcally called 
# once you create your object and it will also capture the location of the your object in self
# class Registration:
#     def __init__(self,name,age,no,gender):
#         self.name=name
#         self.age=age
#         self.no=no
#         self.gender=gender

#     def details():
#         print(f"The student name is {self.name}")

           

# #b=Registration()# ek baar ke baad call karne se constructor function run hoga class sirf ek baar hoga
# std1=Registration("Harsh",22 ,22871393,"male")
# std2=Registration("anchal" ,20,123891386,"Female")
# # print(std1.name)
# # print(std2.name)
# print(std1.details())

#Types if attributes and methods 
#There are 2 types of attributes one is a class attribute and another is a objective/attribute

#There are 3 types of methods
#1> instance/object method(used with keyword like self)- when your method is 
# are getting object location that method is known as instance method

#2> class method - when yoiur method is targetting class location that method is known as class method


#3> Static method - when your are not targetting any location you will use a static method
# class Factory :
#     location="Bhopal"#class attribute

#     def __init__(self,ingredients):
#         self.ingredients=ingredients #instance/object attribute

#     def details(self):#instance/object method
#         print(self.ingredients)

#     @classmethod
#     def factory_info(cls):#class method  
#         print(f"hello your  factory is located in {cls.location}")

#     @staticmethod
#     def hello():
#         print("Hello i am a static method ")


# obj=Factory("icecream")
# obj.hello()

#Constructor (__init__)method -> dunder methods these are called automatically 
