def sum_of_n(n):
    s=0
    n1=1
    for i in range(n):
        s+=n1
        n1+=1
    return s


print(sum_of_n(5))
