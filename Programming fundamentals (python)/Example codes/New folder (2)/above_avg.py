def main():
    num = int(input("Enter a number: "))
    sum = num
    j = 2
    while j<=10:     #10000
        num = int(input("Enter next number: "))
        sum = sum+num
        j = j+1
    print("Average of above numbers", sum/10)

main()
