print("welcome to the Tip Calculator!")
bill = input("what was the total bill? ₹")
tip = input ("how much tip would you like to give?10,12 or 15?")
people = input ("how many people to split the bill?")
bill= float(bill)
tip= int(tip)
people= int(people)
Tip_Amount = (bill/100)*tip
Total_Amount = bill+Tip_Amount
per_person = Total_Amount/people
per_person = round(per_person,2)
print(f"Total Amount of Bill =  {Total_Amount}")
print(f"Bill paid by each person = {per_person}")
