def fun1(a, s):
    i = 0
    while i < s:
        a[i] = i**3
        i = i + 1


def fun2(a, s):
    i = 0
    while i < s:
        print(a[i])
        i = i + 1

def main():
    a = [0] * 1000
    fun1(a, 1000)
    fun2(a, 1000)

    print(type(a))
    print(type(2))
    print(type(None))

main()
