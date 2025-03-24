f = open("4_eof-binfile.py", 'rb')   # remove b from rb and text again

b = f.read(10)
while b:
    print(b)
    print(len(b))
    b = f.read(10)

print("============\nAfter EOF")
print(b)
print(len(b))

f.close()