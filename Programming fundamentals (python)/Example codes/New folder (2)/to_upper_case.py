def upper(s):
    r = ""
    j=0
    while j<len(s):
        if s[j] >= 'a' and s[j] <= 'z':
            r += chr(ord(s[j])-ord('a')+ord('A'))
        else:
            r += s[j]
        j=j+1
    return r

def main():
    name = "iDreEs is 1st oNe"
    print(name)
    name = upper(name)
    print(name)

main()
