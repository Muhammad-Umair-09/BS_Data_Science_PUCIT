r= int(input("Rows: "))
c= int(input("Columns: "))
for i in range(1,r+1):
    for j in range(c):
        print(i,end=" ")
    print()
    for k in range(c):
        print(chr(96+i),end=" ")
    print()

