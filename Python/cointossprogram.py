
from random import randint
print "Starting the program..."
# coin = randint(0,1)
heads =0 # define what randome int will denote heads
headscount=0 #count for tails
tailscount=0 #count for heads
tails =1 # define what randome int will denote heads
count =1 # count for tossing the coin 5000
while count < 5001:
    coin =randint(0,1)
    if coin == 0:
        headscount=headscount+1
        print count,"Attempt Throwing a coin... It's a head! ...Got", headscount, "head(s) so far and",tailscount, "tail(s) so far", coin
    else:
        if coin == 1:
            tailscount=tailscount+1
            print count,"Attempt Throwing a coin... It's a tail! ...Got", tailscount, "tail (s) so far and",headscount,"head (s) so far", coin
    count= count+1
print "Attempt #5000: Throwing a coin... It's a head! ... Got",headscount,"head(s) so far and", tailscount,"tail(s) so far. Ending the program, thank you!"
