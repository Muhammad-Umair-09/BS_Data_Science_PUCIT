def func(s):
    r=""
    i=0
    while i<len(s):
        if (ord(s[i])>47 and ord(s[i])<58):
            r=r+s[i]
        i=i+1
    r=int(r)
    return (r)

print(func("hsudh78,83"))
