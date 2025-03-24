def Sort(a):
    i = 1
    while i < len(a):
        bubble(a)
        i = i + 1
    
def bubble(a):
    i = len(a) - 1
    while i > 0:
        if a[i] < a[i-1]:
            t = a[i]
            a[i] = a[i-1]
            a[i-1] = t
        i = i-1
        
        
def main():
    a = [23, 54, 83, 11, 75, 9, 60, 97, 41]
    print(a)
    Sort(a)
    print(a)
    
    
main()    
