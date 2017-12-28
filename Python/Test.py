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
# def lists (list1, list2):
#     for i in list1:
#         if not list2:
#             lists = True
#         else:
#             if list1[i]==list2[i]:
#                 lists= True
#             else:
#                 lists = False
#                 print" the lists are the same"
# # lists([1,2,5,6,2],[1,2,5,7,2])
# def compare(list1 ,list2):
#     if not identical:
#         lists = False
#     for i in range(len(list1)):
#         if i[list1] == i[list2]:
#             print "the lists are identical"
#         else:
#             print "the lists are not the same"
                # i=[list1]
    # x= [list2]
    # if i[list1] == x[list2]:
    #     print "the lists are identical"
    # else:
     #     print "the lists are not the same"
#print compare ([1,2,3], [1,2,3])

def char_list(word_list, letter):
    newlist=[]
    for word in word_list:
        if letter in word:
            newlist.append(word)
    return newlist

list_with_letter = char_list(["hello","world","my","name","is","mina"], 'o')
print list_with_letter
##Chekerboars###
def checkerboard(arr):
    count=0
    for count in range(0,8):
            print(", " . join(arr))
# checkerboard(["****"])
def checkerboard(arr):
    count =0
    newarr=[]
    for count in range(0,8):
        # print count
        if count %2 == 0:
            print(", " . join(newarr)),(", " . join(arr))
        else:
            print (", " . join(arr))
checkerboard(["****"])
