#treasure hunt, put treasure in a random place.
row1=["◻️","◻️","◻️"]
row2=["◻️","◻️","◻️"]
row3=["◻️","◻️","◻️"]
maap=[row1,row2,row3]
print(f"\n{row1}\n{row2}\n{row3}")
print("where do you want to hide your treasure?")
coloumn=int(input("coloumn (1 to 3) :"))
row=int(input("row (1 to 3) :"))
if coloumn==1:
    if row==1:
        row1[0]="X"
    elif row==2:
        row2[0]="X"
    elif row==3:
        row3[0]="X"
elif coloumn==2:
    if row==1:
        row1[1]="X"
    elif row==2:
        row2[1]="X"
    elif row==3:
        row3[1]="X"
elif coloumn==3:
    if row==1:
        row1[2]="X"
    elif row==2:
        row2[2]="X"
    elif row==3:
        row3[2]="X"
else:
    print("You have entered invalid entries.")
output=print(f"\n{row1}\n{row2}\n{row3}")
