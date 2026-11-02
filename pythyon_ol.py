#OPERATORS 


#ARITHMATIC OPERATORS
#Arithmetic operators works only on datatypes or numbers (int , float,complex)
#(+,-,*,**,//,/,%)
# a=12
# b=34
# print(a+b)#46
# print(a-b)#-22
# #pYTHON FOLLOWS BODMAS rule
# print(a*b)#408(Multiplication )
# print(12/2)#6.0(Normal division)
# print(12//5)#2(Floor division-> will givethe non decimal part)
# print(2**3)#8 (Exponential function ->will give power )
# print(12%7)#5 (Modulus function -> will give the remainder )


#ASSIGNMENT/SHORTHAND OPERATORS 
#(+=,-=,*=,/=,%=,//=)
# a=12
# a+=12#(a=a+12)
# print(a)

# #STRING ALSO USES SOMETHING LIKE THESE OPERATORS 
# #Concatination (+)(Addiiton of two different strings )
# #Multiplication (*)(Can multiply the same string n number of times)
# a="hello"
# b="brother"
# print(a+ b)# will print hellobrother
# print(3*a)#will print hellohellohello

#COMPARISON OPERATORS 
#(==,!=,>,<,>=,<=)
#Result of the comparison operators is always boolean
# a=12
# b=23
# print(a>b)#False
# print(12==12)#True
# print(12!=12)#False
# print(12!=12.1)#True
# print(12>13)#False
# print(12<13)#True
# print(12>12)#False
# print(12>=12)#True
# print((12==12)==True)#True 
# print((12==12)!=True)#False

#LOGICAL OPERATORS(AND / OR / NOT )
#generally used with comparison operators  when more than one comparison operators
# print(12==12 and  56!=45)#True
# print(12==12 and  56>100 and 12==12)#FAlse
# print(12!=12 or 45==89 or 34==44)#FAlse
# print(12==12 or 45==89 or 34==44)#True
# print(not 12==12)#False
# print(not 12==12 == False)#True


#CONTROL FLOW STATEMENTS (IF/ELSE)
#used to control the flow of your program
#Only one condition will work either if or else
#No condition is fitted in else 
#pass is used when you dont want to write anything in else/if box 
# age=int(input("Enter the age :"))
# if age>=18:
#     print(" you can vote")
# else:
#     print("Sorry you cannot vote  ")
# age=int(input("Enter the age :"))
#print("can vote") if age>=18 else print("Cannot vote")(EXAMPLE OF TERNARY OPERATIONS  or if/else statement in one line )
# money=int(input("Enter the money in between 10,20,30, or above="))
# if money==10:
#     print("I WILL HAVE A CHOCOBAR")
# elif money==20:
#     print("I will have a mango dolly")
# elif money==30:
#     print("I will have a cone ")
# else:
#     print("I will have a full course meal")

# a=10
# b=40
# c=30
# if a>b and a>c:
#     print("a is the largest")
# elif b>a and b>c :
#     print("b is the largest ")
# else:
#     print("c is the largest")




