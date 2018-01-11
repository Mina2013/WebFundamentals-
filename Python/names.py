###/***/Print values only/***/
def names(dic1):
    for i in students:
        print i['first_name']
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
names(students)

###/***/ Print enumerated values and length of each value ***/###
def func1(dic):
    count=0
    for key, data in users.items():
        print key
        for i,value in enumerate(data,1):
            count= len(value['first_name']) +len(value['last_name'])
            print i,'-',value['first_name'], value ['last_name'],'-', count
users={
'Students': [
 {'first_name':  'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
],
'Instructors': [
 {'first_name' : 'Michael', 'last_name' : 'Choi'},
 {'first_name' : 'Martin', 'last_name' : 'Puryear'},
 {'first_name' : 'Mina', 'last_name' : 'Aitelhadj'}
]
}
func1(users)
