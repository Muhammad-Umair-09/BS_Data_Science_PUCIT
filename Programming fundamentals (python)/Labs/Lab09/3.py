def non_alphanum(a):
    i=0
    c=0
    while i<len(a):
        x=ord(a[i])
        if x<48 or (x>57 and x<65) or (x>90 and x<97) or x>122:
            c=c+1
        i=i+1
    return c


def main():
    a="jdowi&%$!..."
    a=non_alphanum(a)
    print(a)

main()
