def runLengthEncode(a):
    n=1
    if len(a)==1:
        print(f"{a}:{n}")
    else:
        for x in range(len(a)-1):
            if a[x]==a[x+1]:
                n+=1
            else:
                print(f"{a[x]}:{n}",end="")
                n=1
            x+=1
        print(f"{a[x]}:{n}")


st=input("Enter a string: ")
runLengthEncode(st)
