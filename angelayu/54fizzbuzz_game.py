#the program represents fizzbuzz game.
#The participants sit in a circle.
#In clockwise manner participants will call their position,except if their
#position is divisible by 3, they will say "fizz"
#position divisible by 5, they will say "buzz"
#position divisible by both 3 and 5 will say "fizz-buzz"

total_participants=int(input("The total number of participants are: "))
for number in range(1,total_participants+1):
    if number%3==0 and number%5==0:
        print("fizz-buzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
    else:
        print(number)
