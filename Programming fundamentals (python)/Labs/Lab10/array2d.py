def print2Darray(a, rows, cols):
    r = 0
    while r < rows:
        c = 0
        while c < cols:
            print(a[r][c], end=" ")
            c = c+1
        print()
        r = r+1

def printColMajor2Darray(a, rows, cols):
    c = 0
    while c < cols:
        r = 0
        while r < rows:
            print(a[r][c])
            r = r+1
        c = c+1

def main():
    ROWS = 2
    COLS = 3

    ar = [[0 for c in range(COLS)] for r in range(ROWS)]
    r = 0
    while r < ROWS:
        c = 0
        while c < COLS:
            print("enter value for (", r, ",", c, ") of", ROWS, "X", COLS, "array")
            ar[r][c] = int(input())
            c = c+1
        r = r+1

    print()
    print()

    print2Darray(ar, ROWS, COLS)

    print()
    print()

    printColMajor2Darray(ar, ROWS, COLS)

    print()

main()
