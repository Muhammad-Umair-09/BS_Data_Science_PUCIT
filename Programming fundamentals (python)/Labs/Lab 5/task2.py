meal=float(input("Enter the charges of food: "))
tip=meal/100*15
tax=meal/100*7
print("Charges of food : ", meal)
print("Tip: ", tip)
print("Sales Tax: ", tax)
print("Total amount is", meal+tip+tax)
