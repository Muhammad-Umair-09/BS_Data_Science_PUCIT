import sys

a = 1000

sys.stdout.write("Enter 2 digits: ")
#sys.stdout.flush()
a = sys.stdin.read(4)
b = sys.stdin.read(5)
c = sys.stdin.read(2)

print("a=",a)
print("b=",b)
print("c=",c)

x = sys.stdin.read(2)
print("end", x)

f = open('just_a_file.txt', 'a')
print(a,b,c,sep='#',end='<',flush=False,file=f)
f.close()
