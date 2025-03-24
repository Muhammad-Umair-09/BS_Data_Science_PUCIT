file=open("expenses.txt")
dep=int(input("Number of departments: "))
for i in range(dep):
    x=file.readline()[:-1]
    s=0
    for j in range(7):
        a=file.readline()
        s=s+int(a)
    print(f"{x}: {s}")





