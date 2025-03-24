a=int(input())
b=int(input())
c=int(input())
dis=(b**2)-4*a*c
x1=(-b+(dis**0.5))/(2*a)
x2=(-b-(dis**0.5))/(2*a)
if a==0:
    print("Equation has only one root")
elif dis<0:
    print("Roots are imaginary")
else:
    print(x1,x2)
