#word= "It's Thanksgiving day. It's my birthday, too" .replace('day','month')
#print word
# #print "day"
# x = [2,54,-2,7,12,98]
# #print min(x)
# print max(x)
# def firstlast (arr):
#     first= arr[0]
#     last = arr[len(arr)-1]
#     return (first+last)
# print firstlast(["hello",2,54,-2,7,12,98,"world"])

# x = [19,2,54,-2,7,12,98,32,10,-3,6]
# x.sort()
# print x
# x.append[0]
def separate_plus_minus(x):
    positive = []
    negative = []
    for number in x:
        if number >= 0:
             positive.append(number)
        else:
             negative.append(number)
        return negative[0], positive
    print separate_plus_minus([19,2,54,-2,7,12,98,32,10,-3,6])
