n=int(input("Enter number of people: "))
k=int(input("Enter difference of killing: "))
arr=[]
for i in range(1,n+1):
    arr.append(i)
print(arr)

ind=0
while len(arr)!=1:
    ind+=k-1
    if ind>len(arr):
        while ind > len(arr):
            ind=ind-len(arr)
    if ind==len(arr):
        ind=0
    a=arr.pop(ind)
    print(arr)

print(f"The Survivor is at position {arr[0]} in the circle")



















































#umair
