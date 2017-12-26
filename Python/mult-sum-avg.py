# #this will print odd numbers from 1,1000
# for i in range(1,1000,2):
#     print(i)
# # this will print multips of 5 form 5, to 1,000,000
# for i in range(5,100000):
#     print(i)
#
# #this will sum and average the list
# a= [1,2,5,10,255,3]
# print len(a)
# l=[1,2,5,10,255,3]
# print sum (l)/float(len(l))
# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000.
# Use the for loop and don't use a list to do this exercise.
for i in range(1,1000):
    if i%2==1:
        print i

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for i in range(5,1000000):
    if i%5==0:
        print(i)
# sum and average
a = [1, 2, 5, 10, 255, 3]
sum=0
avg=0
count=0
for i in a:
    sum+=i
    count=count+1
    avg=sum/count
print sum, count, avg
