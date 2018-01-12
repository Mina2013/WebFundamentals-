###/***/This program takes any 2 listes and return a dictionary/****/### 

def func(list1,list2):
    new_dict={}
    new_dict= dict(zip(list1,list2))
    return new_dict
list1 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
list2 = ["salmon","dog","horse", "cat", "spider", "giraffe", "dolphins", "llamas"]
print func((list1),(list2))
