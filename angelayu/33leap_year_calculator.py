#leap year calculator.
#leap year conditions-
#divisible by 4--except-- divisible by 100--unless-- divisible by 400.
print("This is leap year calculator.")
year=int(input("Write a year of your choice:\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")
