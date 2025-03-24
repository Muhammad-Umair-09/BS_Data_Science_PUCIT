for i in range(65,26+65):
    if chr(i)=="A" or chr(i)=="E" or chr(i)=="I" or chr(i)=="O" or chr(i)=="U":
        print(chr(i))
    else:
        print(chr(i),end=" ")
    if chr(i+1)=="A" or chr(i+1)=="E" or chr(i+1)=="I" or chr(i+1)=="O" or chr(i+1)=="U":
        print()
print()
