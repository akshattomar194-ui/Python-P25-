# #Type of Data Structure in Python
# #1.List[] 2.Tupple() 3.Dictionary /Set {}

# #List
# #Hetrogeneou nature-> You can store multiple data type eg:-
# a = ["harsh",28,True,12.2,print()]
# #Indexing -> Same as String

# #mutuable -> you can made changes any value of your  and update also at next step 
# # list # STRING ->You cannnot made changes inside the string
# l = [10,20,30,40,50]
# print(l[1:4]) #Slicing 
# l[0] = 200
# print(l[0:4])

# #Loop on values
# l = [10,20,31,40,50]
# for i in l: #i Variable h jo value ko excess kr rha h 
#     if i%2==0:
#         print(i , end=" ")

#Loops on index
"""
l = [10,20,31,40,50]
for i in range(len(l)): #i Variable h jo value ko excess kr rha h 
    print(i,"->",l[i]) """

#List method
# help(list)
# a.append(40) # It only add a signle element
# print()
# a = [10,20,31,40,50]
# b=a
# b[0] = 1000
# print(a)
# print(b)
# a.extend(range(15)) #can add list,tupple,etc but in 

#Method in Data Structure
"""
print(a.append(40))
print(a.extend(range(15)))
print(a.count(20)) #Return number of occurrences of value
print(a.count(20))  
print(a.insert(1,"uday"))
print(a.remove(50)) # b=a.remove . Remove func does not return a value it means it save a none vale
print(a.reverse())
print(a.sort(reverse=True)) """

# #m=1
# a= [10,20,30,40,50]
# b=[]
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])

# print(b)
# #m=2
# a= [10,20,30,40,50]
# b=[]
# for i in range(len(a),0,-1):
#     b.append(a[i-1])

# print(b)

a= [10,20,30,40,50]
n = len(a)
st = 0
end = n-1
while (st!=n/2) :
    a[i],a[st] = a[end] , a[i]
    
    

print(a)




