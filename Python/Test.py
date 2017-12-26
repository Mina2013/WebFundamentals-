# x= [1,2,3,4,5]
# x.append(99)
# print x
# fruits =['apple','banana','orange']
# Veggie =['lettuce','cucumber','carrots']
# fruits_and_Veggies = Fruits + Veggie
# slad = 3* Veggie
# print salad
# Drawer =['folder','file','pens']
# print Drawer[0] #folder will print
# print Drawer[1] #file will print
# print Drawer[2] #pens will print
#
# my_list =[1,'Zen','hi']
# print len(my_list) # it will print the number or itme in the list 3
#
# # random sales dictionary
# sales = {"apple": 2, "orange": 3, "grapes": 4 }
# print(sales.iterititems())
# print person["favorite_Language"]
# person["favorite_Language"] ="javascript"
# person["name"] ="Dirk"
#
# favoritenumber = [1,2,7,8,"Hello"]
# for i in range(len(favoritenumber)-1,-1,-1):
#     print favoritenumber[i]
# for i in favoritenumber:
#      print favoritenumber
# d={1:'one',2:'two',3:'three'}
# # print 'd.items():'
# for k,v in d.items():
#    if d[k] is v:
#        print "they are the same object'
#         else:
#             print "they are different"
# print 5
# print type (10.25)
# favoritenumbers=[7,4,6,11,13]
# print favoritenumbers[0]
# print favoritenumbers[1]
# print favoritenumbers[2]
# print favoritenumbers[3]
# favoritenumbers[0]=15
# print favoritenumbers
# favoritenumbers.append(20)
#
# mydictionary ={
# "name":"Mina",
# "position":"PM",
# "favorite_Language":"Python"
# }
# print mydictionary["favorite_Language"]
# mydictionary["name"]="Dirk"
# mydictionary["position"]="Manager"
# print mydictionary
# favoritenumbers=[1,131,125.5]
# for i in range(len(favoritenumbers)):
#     # favoritenumbers[i]=10
#     print favoritenumbers[i]
# for i in mydictionary:
#     print mydictionary[i]
# age=22
# if age<20:
#     print"cant come in here"
#     print"must be 21"
# elif "21"==21:
# #     print"this is true"
# set1 =[1,2,3]
# set2 =[11,21,31]
# set3 =[12,23,32]
# def setofinstruction(favoritenumber):
#     favoritenumber[0]=500
#     print favoritenumber
# setofinstruction(set1)
# setofinstruction(set2)
# setofinstruction(set3)
# set1 =[1,2,3]
# def changeparameter(randomParameter):
#      randomParameter[0] =10
#      print randomParameter
# changeparameter(set1)
# # print set,1
# myTuple = (1,2,3)
# myTuple[0]=5
# print myTuple[2]
# words ="it's thanksgiving day. It's my birthday"
# for day in enumerate(words):
#     print (day, words)
# print (words.replace("day", "month"))
# print len(words)
#print (words.replace("day", "month"))
     # print mydictionary[i]
# x=[2,3,44,90]
# print min(x)
# print max(x)

# x=["hello",4,2,15,"world"]
# y=[]
# print x[0]
# print x[len(x)-1]
# y.append(x[0])
# y.append(x[4])
# print y

# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000.
# Use the for loop and don't use a list to do this exercise.
for i in range(1,1000):
    if i%2==1:
        print i

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for i in range(5,1000000):
    if i%5==0:
        print(i)
# sum and average
a = [1, 2, 5, 10, 255, 3]
sum=0
avg=0
count=0
for i in a:
    sum+=i
    count=count+1
    avg=sum/count
print sum, count, avg
