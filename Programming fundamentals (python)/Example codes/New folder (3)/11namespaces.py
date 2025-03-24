def outer_function():
    #global a
    a = 20

    def inner_function():
        #nonlocal a  # nonlocal
        #global a
        a = 30
        print('a in inner function =', a)
        if True:
            j = 90
            # print(j)
        #print(j)    

    inner_function()
    print('a in outer function =', a)

a = 10
outer_function()
print('a as global function=', a)