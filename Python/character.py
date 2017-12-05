def char_list(list):
    char =[]
    newlist=[]
    for i in list:
         for char in i:
            if char == "o":
                print char
                if char in i:
                    print [i]
char_list(["hello","world","my","name","is","mina"])

###Chekerboars###
def checkerboard(arr):
    count=0
    for count in range(0,8):
            print(", " . join(arr))

checkerboard(["****"])
