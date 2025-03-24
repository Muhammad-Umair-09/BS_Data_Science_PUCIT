def minofArray(a,n):
    j=a[0]
    i=0
    while i<n:
        if j>a[i]:
            j=a[i]
        i=i+1
    return j

def main():
    a=[100,76,32,99,67,328]
    print(minofArray(a,len(a)))
main()
