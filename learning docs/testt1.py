import math
x = 0
for y in range(1,50):
    for i in range(1,y+1):
        #print(i,math.floor(i*math.sqrt(2))-i)
        x += math.floor(i*math.sqrt(2))
    print((2*x)/(y*(y+1)))
