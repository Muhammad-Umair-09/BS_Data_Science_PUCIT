f =open("textfile.txt")
a = f.readline()
x=[]
y=[]
while a != "":
    a, b = a.split()
    x.append(float(a))
    y.append(float(b))
    a = f.readline()
print(x,y)

s1=0
for i in range(len(x)):
    s1+=x[i]*y[i]

s2=(sum(x)*sum(y))/len(x)

s3=0
for i in range(len(x)):
    s3+=(x[i])**2

s4=((sum(x))**2)/len(x)

m=((s1-s2)/(s3-s4))
print("m",m)

c=(sum(y)/len(y))-((m)*(sum(x)/len(x)))
print("c",c)

print(f"y= {round(m,2)}x + {round(c,2)}")

