word= "It's Thanksgiving day. It's my birthday, too" .replace('day','month')
print word
#print "day"
x = [2,54,-2,7,12,98]
#print min(x)
print max(x)
print min(x)
def firstlast (arr):
    first= arr[0]
    last = arr[len(arr)-1]
    return (first+last)
# print firstlast(["hello",2,54,-2,7,12,98,"world"])
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first.
# Then, split your list in half. Push the list created from the first half to position 0
# of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98].
# Stick with it, this one is tough!
x= [19,2,54,-2,7,12,98,32,10,-3,6] # print this[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
x.sort()
y=[]
for i in range(len(x)/2):
    y.append(x[0])
    if x[i] < x[len(x)/2]:
        x.pop(0)
x[0]=y
print y
print x
#
# x = [19,2,54,-2,7,12,98,32,10,-3,6]
# def separate_plus_minus(x):
# x.sort()
# print x
# def splitlist(arr):
#     list1=[]
#     list2=[]
#     for i in arr:
#         if i in range(0, len(x)/2):
#             print list1
#
# print separate_plus_minus([19,2,54,-2,7,12,98,32,10,-3,6])
