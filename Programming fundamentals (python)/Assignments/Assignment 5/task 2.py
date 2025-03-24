f_r=open("error free.txt","r+")
f_w=open("grades.txt","r+")
a=(f_r.readline(3)[:-1])
b=(f_r.readline())
while a!="":
    f_w.seek(59*(int(a)-1))
    f_w.write(b)
    a=(f_r.readline(3)[:-1])
    b=(f_r.readline())
f_r.close()
f_w.close()

