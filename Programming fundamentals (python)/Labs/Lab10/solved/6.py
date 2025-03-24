def enterdata():
    a=[[0 for i in range(3)]for j in range(6)]
    j=0
    while j<6:
        i=0
        while i<3:
            print("Enter count of students for program #",j+1, "and shift",i+1)
            a[j][i]=int(input("Enter number of students: "))
            i+=1
        j+=1
    print("\n\n")
    return a

def avrg_stu_in_each_prg(a):
    program=6
    shift=3
    print("Average Students in each program are: ")
    j=0
    while j<program:
        s=0
        i=0
        while i<shift:
            x=a[j][i]
            s=s+x
            i+=1
        avrg=s/shift
        print(f"average students in prg {j+1} is: {avrg}")
        j+=1


avrg_stu_in_each_prg(enterdata())
