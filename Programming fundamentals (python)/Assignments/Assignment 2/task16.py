def GPA(a, b, c, d, e, f, g):
    Sum=0
    s = [a, b, c, d, e, f, g]
    c=[3,1,2,2,1,3,0.5]
    i=0
    while i<7:
        if s[i]=="A":
            gpa=5*c[i]
            Sum= Sum+gpa
        if s[i]=="B":
            gpa=4*c[i]
            Sum= Sum+gpa
        if s[i]=="C":
            gpa=3*c[i]
            Sum= Sum+gpa
        if s[i]=="D":
            gpa=2*c[i]
            Sum= Sum+gpa
        if s[i]=="E":
            gpa=1*c[i]
            Sum= Sum+gpa
        if s[i]=="F":
            gpa=0*c[i]
            Sum= Sum+gpa
        i=i+1
    return Sum/12.5
s = [0]*7
sub = ["PF","PFL","PST","IICT","IICTL","ECC","QT"]
for i in range(7):
    a = input(f"Enter your grade in {sub[i]}")
    s[i] = a
print(GPA(s[0], s[1], s[2], s[3], s[4], s[5], s[6]))
