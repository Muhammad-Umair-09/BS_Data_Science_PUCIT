def printNchars(n, c):
    j = 1
    while j <= n:
        print(c, end="")
        j = j+1
    return
    
def printSquare(n, c):    
    j = 1
    while j <= n:
        printNchars(n, c)
        print()
        j = j+1
    return

def printTriangle(n, c):    
    j = 1
    while j <= n:
        printNchars(j, c)
        print()
        j = j+1
    return
    
def main():
    printSquare(5,'*')
    printTriangle(8, '@')
    return
    
main()
