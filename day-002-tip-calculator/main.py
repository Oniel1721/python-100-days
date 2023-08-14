print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
billAndTip = totalBill + ( tipPercentage/100 * totalBill )
payPerPerson = billAndTip / people

print(f"Each person should pay: ${str(round(payPerPerson, 2))}")