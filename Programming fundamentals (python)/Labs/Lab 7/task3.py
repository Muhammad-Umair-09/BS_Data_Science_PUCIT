def sumArray(a,n):
    i=0
    sum=0
    while i<n:
        sum=sum+a[i]
        i=i+1
    return sum
def main():
    a=[1,2,3,4,5]
    p=sumArray(a,len(a))
    print(p)
main()
