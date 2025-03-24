def pad(s):
    s1=" "*(16-len(s))
    x=s+s1
    return x

file = open("contact.txt","w")
for i in range(1):
    n=input("Name: ")
    n=pad(n)
    p=input("Number: ")
    p=pad(p)
    e=input("Email: ")
    file.write(f"{n} {p} {e}\n")

for i in range(0):
    n=input("Name: ")
    p=input("Number: ")
    e=input("Email: ")
    file.write(f"{n},{p},{e}\n")

file.close()
