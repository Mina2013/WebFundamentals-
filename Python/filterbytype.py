def int (x):
    if x < 100:
        print "number is small"
    else:
        print "number too big"
int(600)
def sentence (string):
    if len(string) < 50:
        print "short sentence"
    else:
        print "this is long sentence"
sentence("tell me and I forget. Teach me and I remenmber, invole me and i learn")

def mylist(arr):
    if len(arr) >= 10:
        print "Big List"
    else:
        print "Short list"
mylist ([1,2,5,8,"hello"])
#check for int type
x= 100
if isinstance(x, int):
    print "x is an int"
    if x < 100:
        print "this number small"
    else:
        print "this number is big"
#check for sting type
y= "tell me mote about how we can get along and work through this"
if isinstance(y, str):
    print "y is an string"
    if len(y) < 50:
        print "this is a short sentence"
    else:
        print "this is a long sentence"
#check for list type
z= [10,12,"hello",3,23,20,974,1,"social",2,23]
if isinstance(z, list):
    print "Z is an list"
    if len(z) < 10:
        print "short list"
    else:
        print "Long list"
