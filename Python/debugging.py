def mutiply(arr,num):
    print arr, num
    for x in arr:
        print x
        x *=num
        print arr
    return arr
a = [2,4,10,16]
b = mutiply(a,5)
print b

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
        return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
