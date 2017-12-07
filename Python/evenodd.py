# def evenodd(x,y):
#     count =0
#     for count in range(x,y):
#         if count %2 == 0:
#             print "number is", count, "this is an even number"
#         else:
#             if count %2 == 1:
#                 print "number is", count, "this is an odd number"
# print evenodd(0,2001)
#
# ### Multiply###
# def multiply(arr,z):
#     for x in arr:
#         x *=z
#         #print arr
# a=[2,4,10,16]
# b= multiply (a,5)
# print b

####2dimentional####
def layered_multiples(arr,num):
    for x in arr:
        multiply= x*num
     # your code here
 # return new_array
x = layered_multiples([2,4,5],3)
print x
print multiply
