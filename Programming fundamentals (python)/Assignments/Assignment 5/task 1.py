def pad(s):
    s=str(s)
    return((2-len(s))*" ")+s
f=open("grades.txt","r+")
f1=open("error free.txt","w")
(f.readline())
(f.readline())
c=0
line=3
a=(f.readline())
while a!="":
    x=0
    i=0
    while i<4 and x==0:
        if (ord(a[i])>=65 and ord(a[i])<=90) or (ord(a[i])>=97 and ord(a[i])<=122):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        i+=1
    j=4
    while j<6 and x==0:
        if (ord(a[j])>=48 and ord(a[j])<=57):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        j+=1
    k=6
    while k<7 and x==0:
        if (ord(a[k])>=65 and ord(a[k])<=90) or (ord(a[k])>=97 and ord(a[k])<=122):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        k+=1
    l=7
    while l<10 and x==0:
        if (ord(a[l])>=48 and ord(a[l])<=57):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        l+=1
    m=10
    while m<42 and x==0:
        if (ord(a[m])>=65 and ord(a[m])<=90) or (ord(a[m])>=97 and ord(a[m])<=122) or (a[m]==" "):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        m+=1
    n=42
    while n<44 and x==0:
        if (ord(a[n])>=65 and ord(a[n])<=90) or (ord(a[n])>=97 and ord(a[n])<=122):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        n+=1
    o=49
    while o<51 and x==0:
        if (ord(a[o])>=48 and ord(a[o])<=57):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        o+=1
    p=52
    while p<54 and x==0:
        if (ord(a[p])>=48 and ord(a[p])<=57):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        p+=1
    q=55
    while q<57 and x==0:
        if (ord(a[q])>=48 and ord(a[q])<=57):
            pass
        else:
            c+=1
            x+=1
            f1.write(f"{pad(line)}.{a}")
            break
        q+=1
    line+=1
    a=(f.readline())
print("Number of lines having error are:",c)
f1.close()
f.close()
