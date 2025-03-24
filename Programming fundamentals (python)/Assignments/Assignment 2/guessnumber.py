from random import *
x=randint(1,10)
i=1
is_done = False
while i<=3 and is_done==False:
    a=int(input())
    if a==x:
        print("Winner")
        is_done = True
    i=i+1
if is_done==False:
    print("Loser", x)
