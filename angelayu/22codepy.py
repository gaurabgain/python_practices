#calculate bmi in integers
weight=int(input("Your weight in kilogram: \n"))
height=int(input("Your height in centimeters: \n"))
bmi=int((weight*10000)/(height**2))
print("Your bmi is:",str(bmi))
