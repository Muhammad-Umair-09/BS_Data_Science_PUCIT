import random
i=0
ln=22
a=[None]*ln
while i<ln:
    a[i]=random.randint(1,10)
    i=i+1
print(a)

def func(a):
    b=[None]*len(a)
    s=0
    i=0
    while i<len(a):
        s=s+a[i]
        avrg=round(s/(i+1),2)
        b[i]=avrg
        i=i+1
    return b

def main():
    a = [1, 2, 3, 4, 5]
    print(func(a))
main()


