def namesearch(a,n,x):
    i=0
    j=False
    while i<n:
        if x==a[i]:
            j=True
        i=i+1
    return j

def main():
    x=(input("Enter your friend's name: "))
    a=["ali","akbar","hamza","umair","najam","aqeel","talha","zahoor"]
    print(namesearch(a, len(a), x))

main()
