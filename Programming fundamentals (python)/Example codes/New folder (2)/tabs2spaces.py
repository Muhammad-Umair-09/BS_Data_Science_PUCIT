def tab2spaces(s):
    r =""
    i=0
    while i < len(s):
        if s[i] == "\t":
            r = r+"   "
        else:
            r = r+s[i]
        i=i+1
    return r

def main():
    st = "eman\tzahid"
    print(ascii(st))
    p = tab2spaces(st)
    print(ascii(p))

main()
