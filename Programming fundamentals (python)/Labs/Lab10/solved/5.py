def main():
    program = 6
    shift = 3
    a = [[0 for i in range(shift)] for j in range(program)]
    j = 0
    while j < program:
        i = 0
        while i < shift:
            print("Enter count of students for program #", j, "and shift", i)
            a[j][i] = int(input("Enter number of students: "))
            i += 1
        j += 1
    return a


print(main())
