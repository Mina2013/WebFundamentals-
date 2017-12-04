# tuple_data = ('physics','Chemestry', 1998,2000)
# tuple_num = (1,2,3,4)
# tuple_letter = "s","a","m"
# dog =("hello there", "dog", "cat", 12)
# print dog[2]
# dog = dog +("domesticated",)
# dog = dog[:3]+("man's bff",)+dog[4:]
# for data in dog:
#     print data
#dog[0]="X" # cannot change values in tupple

# dictionary
# weekend = {"sun": "sunday","sat":"saturday"}
# capital = {}
# capital["alg"] = "Algiers"
# capital["fra"] = "Paris"
# capital["dnk"] = "copenhagen"
# print weekend["sun"]
# # for data in capital:
# #     print data
# # for key in capital.iterkeys():
# #     print key
# # for val in capital.itervalues():
# #     print val
# for key,data in capital.iteritems():
#     print key, "=", data
context = {
'question':[
{'id':1, 'content': 'Why is there snow?'},
{'id':2, 'content': 'Why is ther lightening?'},
{'id':3, 'content': 'Whose your daddy?'}
]
}
for key,data in context.items():
    for value in data:
        print "Question#", value["id"],":", value["content"]
        print "---"
data = {"house":"maison","dog":"chein","red":"rouge"}
print data.items()
print data.keys()
print data.values()
