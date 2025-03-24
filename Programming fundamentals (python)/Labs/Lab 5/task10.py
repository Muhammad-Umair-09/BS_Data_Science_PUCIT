def falling_distance(t):
    d=round(((9.8*t*t)/2),2)
    return d

i=1
while i<=10:
    print(falling_distance(i))
    i=i+1
