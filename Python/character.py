def char_list(list):
    char =[]
    for i in list:
         for char in i:
            if char == "o":
                print char
                if char in i:
                    print [i]
char_list(["hello","world","my","name","is","mina"])
print char
