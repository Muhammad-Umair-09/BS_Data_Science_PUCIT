def pad(s,x,c,p):
    if p=="r":
        s1=str(c)*(x-len(s))
        x=s+s1
    if p=="l":
        s1=str(c)*(x-len(s))
        x=s1+s
    if p=="m":
        s1=str(c)*(x-len(s))
        z=int(len(s)/2)
        s0=""
        for i in range(z):
            s0+=s[i]
        s0=s0+s1
        for i in range(z,len(s)):
            s0+=s[i]
        x=s0
    return x

s=input("Enter a string for padding: ")
p=input("Enter the position of padding as l,r or m: ")
f=input("Figure to use for padding: ")
l=int(input("Enter max length for a padded number: "))
print(pad(s,l,f,p))

