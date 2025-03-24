a=["PF","DS","PST","Quran","ICT","Eng"]
m=[30,25,32,35,33,31]
f=[36,31,34,35,38,39]
s=[24,23,22,19,25,25]

i=0
while i<6:
    t=m[i]+f[i]+s[i]
    print(a[i],t)
    i=i+1
print("Avrg of Mid=",sum(m)/6)
print("Avrg of Final=",sum(f)/6)
print("Avrg of Sessional=",sum(s)/6)
print("Avrg of Total=",((sum(m)/6)+(sum(f)/6)+(sum(s)/6))/3)
