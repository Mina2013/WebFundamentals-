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
