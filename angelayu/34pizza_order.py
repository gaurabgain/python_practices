#a pizza order program.
#pizza sizes, small $15, medium $20, large $25.
#paperoni small $2, medium and large $3.
#extra cheese $1.

print("Welcome to python pizza.")
size=input("Which size pizza would you like to order?\nS(small),M(medium),L(large)\n")
paperoni=input("Do you want paperoni?\nY/N\n")
cheese=input("Do want cheese?\nY/N\n")
if size=="S":
    if paperoni=="Y":
        if cheese=="Y":
            print("Price of your order is $18.")
        else:
            print("Price of your order is $17.")
    else:
         print("Price of your order is $15.")
elif size=="M":
    if paperoni=="Y":
        print("Price of your order is $23.")
    else:
        print("Price of your order is $20.")
else:
    if paperoni=="Y":
        print("Price of your order is $28.")
    else:
        print("Price of your order is $25.")
