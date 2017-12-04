def list_type (list):
    #print list
    total = 0
    for x in list:
        #print x
        if type (x) == int:
            total+= x
            #print "this is an integer"
            print "sum", total
        else:
            if type (x) == str:
                print "sting:", x
        if isinstance (list, str):
            print "this is a list of strings"
        else:
            if isinstance (list, int):
                print "this is a list of numbers"
            else:
                print "this is a mixed list"
        # else:
         #     if isinstance (list, int):
         #         print "this is a list of numbers"
list_type ([1,2,3,])
