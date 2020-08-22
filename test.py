from random import*


for x in range(1,6):
    print( " " * x + ("*"*x) )
    for y in range(1,6):
        r = randint(0,99)
        print(" " * y+("*"*r))


if(r==0):
    print("Start")
elif(r==99):
    print("End")
else:
    print("Keep")


