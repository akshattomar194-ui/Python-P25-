#ENCAPSULATION-MAKING THE DEATILS PRIVATE 
#Agar ek class me agar constructor function bannaya hai 
# then jab bhi uska object banega sabse pehle constructor chalega 
# class Student :
#     def __init__(self):
#         print("AGain a constructor")

#     def show(self):
#         print("YEh hai show function")

#     def __init__(self):
#         print("Yeh hai constructor ")

# obj=Student()
# obj.show()


# class Student:
#     def __init__(self):
#         self.a="Hello"#Public attribute-can  be used anywhere
#         self._b=22#Protected attribute-
#         self.__name="Sheryians"#Private attribute -cannot be used outside of the class 

#     def show_attribute(self):##Getter method
#         print(self.__name)

#     def change_attribute(self,name):#Setter method 
#         self.__name=name

#     def  __secret(self):#Private Method 
#         print("This is a private method ")

#     def show_method(self):
#         self.__secret()

# obj=Student()
# obj.show_method()
# print(obj.a)
# print(obj._b)
# obj.change_attribute("nyc")
# # print(obj.__c)
# obj.show_attribute()


#DATA ABSTRACTION- 
# from abc import ABC ,abstractmethod
# class Template(ABC):#ABstract base class /Template  class
#     @abstractmethod
#     def show(self):
#         pass

#     def display(self):
#         print("This is a template class ")

# class base(Template):
#     def show(self):
#         print("This is the base class")

# obj=base()
# obj.show()
# obj.display()

from abc import ABC ,abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

    def show(self):
        print("This is payment class")

class UPI(Payment):
    def pay(self,amount):
        self.amount=amount
        print(f"Ammount done {self.amount}")

class Card (Payment):
    def pay(self,amount):
        self.amount=amount
        print(f"Payed by  card {self.amount}")

obj=UPI()
obj2=Card()
obj2.pay(10000)
obj2.show()
obj.pay(100)
obj.show()