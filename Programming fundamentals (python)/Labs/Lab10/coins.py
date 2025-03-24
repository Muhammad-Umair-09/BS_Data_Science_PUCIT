class coin:
    cent = 1
    dime = 10
    quarter = 25
    dollar = 100

def inputCoin():
    t = input()
    if t == "cent":
        return coin.cent
    if t == "dime":
        return coin.dime
    if t == "quarter":
        return coin.quarter
    if t == "dollar":
        return coin.dollar

def printCoin(c):
    if c == coin.cent:
        print("cent")
    if c == coin.dime:
        print("dime")
    if c == coin.quarter:
        print("quarter")
    if c == coin.dollar:
        print("dollar")

def main():

    print("Enter three coin names one by one")
    print("all different, two same, all same")
    c1 = inputCoin()
    c2 = inputCoin()
    c3 = inputCoin()

    if c1 == c2:
        print("You enter first two same coins")
    else:
        print("You enter first two different coins")

    print("Third coin you entered is")
    printCoin(c3)

main()


