# strings are like arrays but readonly

def bb(s):
    #s[1] = "B"
    print(s[1])

def main():
    h = "XYZ"
    print(h)  # displays XYZ
    bb(h)  # changes first letter to A
    print(h)  # displays AYZ

main()
