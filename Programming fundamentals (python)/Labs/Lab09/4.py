def alpha(s):
    i=0
    r=False
    while i<(len(s)-1):
        x=ord(a[i])
        if (x==44 or (x>64 and x<91) or (x>96 and x<123) or x==32 or x==9):
            r=True
        else:
            r=False
            return r
        i=i+1
    if (ord(s[len(s)-1]))==46:
        return r
    else:
        r==False
    return r


a="hsdhJH."
print(alpha(a))
