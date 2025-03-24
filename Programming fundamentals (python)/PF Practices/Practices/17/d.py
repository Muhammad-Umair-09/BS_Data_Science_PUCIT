r= int(input("Rows: "))
c= int(input("Columns: "))
for i in range(r):
    for j in range(1+i,c+1+i):
        print(j,end=" ")
    print()
