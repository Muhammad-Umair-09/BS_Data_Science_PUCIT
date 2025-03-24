def pad(s,l,m):
    s=str(s)
    return (" "*l)+s+(" "*(m-len(s)-l))

def grade(a):
    a=float(a)
    if a>=85:
        g="A"
    elif a>=80:
        g="A-"
    elif a>=75:
        g="B+"
    elif a>=70:
        g="B"
    elif a>=65:
        g="B-"
    elif a>=61:
        g="C+"
    elif a>=58:
        g="C"
    elif a>=55:
        g="C-"
    elif a>=50:
        g="D"
    else:
        g="F"
    return " "+g



f=open("grades.txt")
bse_n=4#int(input("Enter number of students in BSE, in grades file are \"4\": "))
bit_n=3#int(input("Enter number of students in BIT, in grades file are \"3\": "))

print(" "*25+"Univerdity of the Punjab")
print(" "*21+"College of Information Technology")
print(" "*23+"Result Session : Spring 2010\n")


print(f"Degree : BSE\n")
print(f"Sr.No. Roll No.   Student Name                   ITC  PF   DLD  Total %age Grade")
print(f"====== ========== ============================== ===  ===  ===  ===== ==== =====")

arr_bse=[]
for i in range(0,bse_n*59*3,59*3):
    arr=[]
    for j in range(3):
        f.seek((59*2)+i+(59*j)+49)
        arr.append(sum(list(map(int,f.readline().split()))))
    arr_bse.append(arr)


sr=1
for j in range(bse_n):
    print(pad(sr,3,6),end="")#sr
    f.seek(59*2+(3*59*j))
    print(pad(f.readline(10),1,11),end="")#roll no.
    print(pad(f.readline(31),1,31),end="")#name
    print(pad(arr_bse[j][0],0,4),pad(arr_bse[j][1],0,4),pad(arr_bse[j][2],0,4),pad((sum(arr_bse[j])),1,5),round((sum(arr_bse[j])/3),1),grade((sum(arr_bse[j])/3)))
    sr+=1


print(" "*49+"===============================")
print(" "*28+"BSE Degree Average:  ",end="")
all_avg=[]#overall average of departmnets
bse_avg=[]
sm=0
for i in range(3):
    s=0
    for j in range(bse_n):
        s+=(arr_bse[j][i])
    s=int(s/bse_n)
    bse_avg.append(s)
    sm+=s
    print(s,end="   ")
print(pad(sm,1,5))
all_avg.append(sm)



















print()
print(f"Degree : BIT\n")
print(f"Sr.No. Roll No.   Student Name                   ITC  PF   DLD  Total %age Grade")
print(f"====== ========== ============================== ===  ===  ===  ===== ==== =====")

arr_bit=[]
for i in range(0,bit_n*59*3,59*3):
    arr=[]
    for j in range(3):
        f.seek((59*2)+i+(59*j)+49+(bse_n*59*3))
        (arr.append(sum(list(map(int,f.readline().split())))))
    arr_bit.append(arr)


sr=1
for j in range(bit_n):
    print(pad(sr,3,6),end="")#sr
    f.seek(59*2+(3*59*j)+(bse_n*59*3))
    print(pad(f.readline(10),1,11),end="")#roll no.
    print(pad(f.readline(31),1,31),end="")#name
    print(pad(arr_bit[j][0],0,4),pad(arr_bit[j][1],0,4),pad(arr_bit[j][2],0,4),pad((sum(arr_bit[j])),1,5),round((sum(arr_bit[j])/3),1),grade((sum(arr_bit[j])/3)))
    sr+=1


print(" "*49+"===============================")
print(" "*28+"BIT Degree Average:  ",end="")
bit_avg=[]
sm=0
for i in range(3):
    s=0
    for j in range(bit_n):
        s+=(arr_bit[j][i])
    s=int(s/bit_n)
    bit_avg.append(s)
    sm+=s
    print(s,end="   ")
print(pad(sm,1,5))
all_avg.append(sm)








print("\n")
print(" "*30+"Over All Average:  ",end="")
for i in range(len(bse_avg)):
    print(int((bse_avg[i]+bit_avg[i])/2),end="   ")
print(end=" ")
print(int(sum(all_avg)/2))









