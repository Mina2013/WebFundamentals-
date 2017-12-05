def list_type (list):
    total = 0
    ismixed = True
    for x in list:
        if type (x) == int or type (x) ==float:
            total+= x
            print "sum", total
        else:
            if type (x) == str:
                print "sting:", x
    for y in range(len(list)):
        if isinstance (y, str):
            print "this is list of words"
        else:
            if isinstance (y, int):
                print "this is a list of numbers"
            else:
                print "this is a mixed list"

list_type (["hello",10.0,0,1,2])
