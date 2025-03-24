def search(x,a,start,end):
    i=start
    while i<=end:
        if x==a[i]:
            s=i-start
            return s
        i=i+1
def main():
    a=["ali","akbar","hamza","umair","najam","aqeel","talha","zahoor"]
    x=input("Enter your friend's name: ")
    s=int(input("Enter the starting point from 0 to onward but less than array's size: "))
    e=int(input("Enter the ending point: "))
    print(search(x,a,s,e))
main()
