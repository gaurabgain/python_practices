#bill split between x people, tip is y%
bill = float(input("What is the bill amount?\n"))
people = int(input("No of people?\n"))
tip = int(input("tip percentage : \n"))
bill_total= bill+tip/100*bill
bill_per_person= round(bill_total/people ,2)
print(f"The bill amount per person is ${bill_per_person}")
