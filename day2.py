print("welcom to tip calculator")
totalBill=float(input("what was the total bill? $"))
print(totalBill)
tip=int(input("how much tip would you like to give? 10,12 or 15?\n"))
spilitePeople=int(input("split with how much people?\n"))
tip_as_percent=tip/100
total_tip_amount=totalBill*tip_as_percent
billPerPerson=totalBill/spilitePeople
final_amount=round(billPerPerson,2)
print(f"each person should pay: {final_amount}")
