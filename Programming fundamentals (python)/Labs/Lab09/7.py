def main():
    a=[None]*100
    i=0
    z=0
    print(z)
    x=True
    b=input()
    if b=="stop":
        x=False
    if b=="+":
        c=int(input())
        z=(z+c)
        print(z)
        a[i]=z
    if b=="-":
        c=int(input())
        z=(z-c)
        print(z)
        a[i]=z
    while x==True:
        b=input()
        if b=="initialize":
            main()
        if b=="stop":
            x=False
        if b=="+":
            c=int(input())
            z=(z+c)
            print(z)
            i=i+1
            a[i]=z
        if b=="-":
            c=int(input())
            z=(z-c)
            print(z)
            i=i+1
            a[i]=z
        if b=="/":
            c=int(input())
            z=(z/c)
            print(z)
            i=i+1
            a[i]=z
        if b=="*":
            c=int(input())
            z=(z*c)
            print(z)
            i=i+1
            a[i]=z
        if b=="**":
            c=int(input())
            z=(z**c)
            print(z)
            i=i+1
            a[i]=z
        if b=="%":
            c=int(input())
            z=(z%c)
            print(z)
            i=i+1
            a[i]=z
        if b=="last":
            if (i-1)>=0:
                i=i-1
                z=(a[i])
                print(z)
            else:
                print("Nothing you have computed before it")
main()
j=0
while j==0:
    a=input("write 'initialize' to start: ")
    if a=="initialize":
        main()

