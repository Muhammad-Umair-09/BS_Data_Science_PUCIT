class salah():
    tahajjud=1
    fajar=2
    ishraq=3
    chasht=4
    zuhur=5
    asr=6
    magrib=7
    awabeen=8
    isha=9

def inputsalah():
    a=input("Enter salah name: ")
    if a=="tahjjud":
        return salah.tahajjud
    if a=="fajar":
        return salah.fajar
    if a=="ishraq":
        return salah.ishraq
    if a=="chasht":
        return salah.chasht
    if a=="zuhur":
        return salah.zuhur
    if a=="asr":
        return salah.asr
    if a=="magrib":
        return salah.magrib
    if a=="awabeen":
        return salah.awabeen
    if a=="isha":
        return salah.isha
def output(x):
    if x==1:
        return "tahajjud"
    if x==2:
        return "fajar"
    if x==3:
        return "ishraq"
    if x==4:
        return "chasht"
    if x==5:
        return "zuhur"
    if x==6:
        return "asr"
    if x==7:
        return "magrib"
    if x==8:
        return "awabeen"
    if x==9:
        return "isha"

def main():
        x=inputsalah()
        y=output(x)
        print(y,"=",x)


main()

