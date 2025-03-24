pen=float(input("Enter the number of Pennies: "))
nic=float(input("Enter the number of Nickles: "))
dim=float(input("Enter the number of Dimes: "))
qua=float(input("Enter the number of Quarters: "))
pen=pen/100
nic=nic/20
dim=dim/10
qua=qua/4
dollar=(pen+nic+dim+qua)
if dollar==1:
    print("Congratulations! You have won")
else:
    print("Whether the amount entered was more than or less than one dollar")
