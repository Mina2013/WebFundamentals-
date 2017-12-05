def compare(list1 ,list2):
    i=[]
    isidentical = False
    for i in range(len(list1)):
        print i
        if i[list1] == i[list2]:
            isidentical = True
            print "the lists are identical"
        else:
            print "the lists are not the same"
                # i=[list1]
    # x= [list2]
    # if i[list1] == x[list2]:
    #     print "the lists are identical"
    # else:
    #     print "the lists are not the same"
compare ([1,2,3], [1,2,3])
