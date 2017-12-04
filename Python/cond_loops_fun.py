def add (a,b):
    x = a + b
    return x
result = add(3,5)
#result = add("truck","car ")
print result

def say_hi(name):
    print "hi,"+ name
    say_hi("Mina")

def say_hi():
    return "Hi"
greeting =say_hi()
print greeting

for count in range(0,5):
    print "looping-", count
age = 10
if age >= 21:
    print 'legal age'
elif age == 12:
    print 'too young'
else:
    print 'baby'

list = [4,"hello",99, ["apple","potatoe"], "world"]
for element in list:
     print element
count =0
while count <5:
    print "looping-", count
    count +=1

for val in "string":
    if val == "i":
        #break
        continue
    print val

def add(a, b):
    x = a + b
    return x
sum1 = add(1,2)
sum2 = add(5,5)
sum3 = sum1 + sum2
def get_circle_area(r):
    c = 2 * math.pi * r
    a = math.pi *r*r
    return (c,a)
get_circle_area (10)
