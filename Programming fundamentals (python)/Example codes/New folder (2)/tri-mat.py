def main():
    n = int(input("Enter dimensions of Square Matrix: "))
    i = 0
    while i < n:
        j = 0
        while j <= i:
            k = n*j - j*(j-1)//2 + (i-j)
            print(j, ",", i , "=>", k)
            j = j+1
        i = i+1

main()
