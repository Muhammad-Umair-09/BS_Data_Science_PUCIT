ar1 = [12, 4, 6, 3, 9, 32]
ar1size = len(ar1)

j = 0
while j < ar1size:
    print(ar1[j])
    j = j+1
    
ar2 = [None] * 5
ar2size = len(ar2)     # or simply 5

j = 0
while j < ar2size:
    ar2[j] = input("Enter a country name: ")
    j = j+1

print(ar2)
# but we should use loop to print the array contents