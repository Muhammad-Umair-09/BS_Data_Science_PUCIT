import random
ar = [[[random.randint(10, 100)for i in range(5)]for n in range(4)]for x in range(6)]
print(ar)
#for year 2023 at index4
def dep_wise_max(a):
    for j in range(4):
        x=max(a[4][j])
        print("max of Dep",j,x)
dep_wise_max(ar)

print("========")
#for dep IT at index1 and certificate Web Develop at index3
def year_wise_max(a):
    x=(a[0][1][3])
    for j in range(1,6):
        y=(a[j][1][3])
        if x>y:
            x=y
    return x
x=year_wise_max(ar)
print("year wise min",x)




