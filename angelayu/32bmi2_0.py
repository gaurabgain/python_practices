#bmi calculator v2.0
weight=float(input("Write your weight in kg: "))
height=float(input("Write your height in meters: "))
bmi=round(weight/height**2,2)
print(f"Your bmi is {bmi}")
if bmi < 18.5 :
    print("You are underweight.")
elif bmi < 25 :
    print("You have a normal weight.")
elif bmi < 30 :
    print("You are slightly overweight.")
elif bmi < 35 :
    print("You are obese.")
else:
    print("You are clinically obese.")
