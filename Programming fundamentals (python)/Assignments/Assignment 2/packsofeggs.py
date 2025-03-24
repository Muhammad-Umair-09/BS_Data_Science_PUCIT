e= int(input("Enter the number of eggs: "))
q=e//6
r=e%6
if r==0:
    print("Packs of eggs required are: ", q)
else:
    print("Packs of eggs required are: ", q+1)
