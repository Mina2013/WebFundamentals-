def char_list(word_list, letter):
    newlist=[]
    for word in word_list:
        if letter in word:
            newlist.append(word)
    return newlist

# for i in range(0, len(word)):
#     print word[i]

# for letter in word:
#     print letter

list_with_letter = char_list(["hello","world","my","name","is","mina"], 'w')
print list_with_letter
###Chekerboars###
def checkerboard(arr):
    count=0
    for count in range(0,8):
            print(", " . join(arr))

checkerboard(["****"])
