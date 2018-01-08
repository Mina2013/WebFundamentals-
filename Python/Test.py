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
# l = ['magical unicorns',19,'hello',98.98,'world']

# l = [2,3,1,7,4,12]
# # l= ['magical','unicorns']
# # l = ['magical unicorns',19,'hello',98.98,'world']
# sum=0
# for i in range(len(l)):
#     if isinstance(l, int):
#         print "this is a list of integers"
#     #     print "Sum is", sum
#
#
# #    else:
# #         if isinstance(l, str):
# #             print "this is list of stings"
# # print "Stings:", l[i]
# # print "sum:", sum
# # print "this is a list of integer types"
# # print "sum is:", sum
# #     if isinstance(l, int):
# #     print "x is a list integer"
# #  else:
# # #         if isinstance(l, str):
# #             print"this is a list of strings"
# #         else:
# #             if isinstance(l, list):
# #                 print " this is a list"
# l = [2,3,1,7,4,12]
# # sum=0
# l= ['magical','unicorns']
# # l = ['magical unicorns',19,'hello',98.98,'world']
# # for i in range(len(l)):
# #     if isinstance(l[i], int):
# #         sum=sum+l[i]
# # print "this is a list of int"
# # print "Sum:", sum
# for i in range(len(l)):
#     # print l[i]
#     if isinstance (l, str):
#
#         # print "this is a list of strings"
# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]
# for i in range (1,2000):
#         if i%2==0:
#             print "the Number is Even", i
#         elif i%2==1:
#             print "the Number is Odd",
#
# a = [2, 4, 10, 16])
# def multiply(a, num):
#     for i in a:
#         a=i*num
#         print a
# multiply([2,4,5],5)
#
# def layered_multiples(arr,num):
#     new_arr=[]
#     for i in arr:
#         new_arr.append(i*num)
#     print new_arrf
 # arr=arr*Num
    # arr.append(arr)
    # print arr
#     # for i in range(len(arr)):
        # print i, arr
# layered_multiples([2,4,5],3)
# print x
# from random import randint
# grade = randint(0,100)
# print "Scores and Grades"
# if grade < 60:
#     print"Score:", grade, "; Your grade is F"
# else:
#     if grade>60 and grade<=69:
#         print "Score:", grade, "; Your grade is D"
#     else:
#         if grade>69 and grade<=79:
#             print "Score:", grade, "; Your grade is C"
#         else:
#             if grade>79 and grade<=89:
#                 print "Score:", grade, "; Your grade is B"
#             else:
#                 if grade>89 and grade<=100:
#                     print "Score:", grade, "; Your grade is A"
# print "End of the program. Bye"


from random import randint
print "Starting the program..."
# coin = randint(0,1)
heads =0 # define what randome int will denote heads
headscount=0
tailscount=0
tails =1
count =1
while count < 5001:
    coin =randint(0,1)
    if coin == 0:
        headscount=headscount+1
        print count,"Attempt Throwing a coin... It's a head! ...Got", headscount, "head(s) so far and",tailscount, "tail(s) so far", coin
    else:
        if coin == 1:
            tailscount=tailscount+1
            print count,"Attempt Throwing a coin... It's a tail! ...Got", tailscount, "tail (s) so far and",headscount,"head (s) so far", coin
    count= count+1
print "Attempt #5000: Throwing a coin... It's a head! ... Got",headscount,"head(s) so far and", tailscount,"tail(s) so far. Ending the program, thank you!"
