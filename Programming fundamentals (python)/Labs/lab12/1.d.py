n=5#int(input())
x=0
for i in range(n):
    if x==10:
        x=0
    for j in range(x,x+1+i):
        print(x,end="")
        x+=1
    print()

