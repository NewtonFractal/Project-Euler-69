import time
import math
start = time.time()
primelist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

def Totient_maximum(number,start):
    for x in primelist:
        if start*x < 1000000:
            start *= x
        else:
            print(start)
            break

Totient_maximum(1000000,1)

end = time.time()
print(end - start)