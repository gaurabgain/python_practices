#this is a pizza ordering program.
#size and price of pizza - small $15, medium $20, large $25.
#paperoni for - small +$2, medium & large +$3.
#cheese for +$1.
print("Welcome to python pizza.")
size=input("Which size of pizza do you want?\nS(small),M(medium),L(large)\n")
paperoni=input("Do you want paperoni?\Y/N\n")
cheese=input("Do you want cheese?\nY/N\n")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25

if paperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if cheese=="Y":
    bill+=1

print(f"Your bill is ${bill}.")
