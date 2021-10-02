#love calculator
"""
This is a love calculator. It take your and your partner's name and makes a
two digit love score by concating the sum of letters "t,r,u,e" and "l,o,v,e" in
both of those names.
"""
print("Welcome to love calculator.\n")
name1=input("What is your name?\n").lower()
name2=input("What is their name?\n").lower()
t=name1.count("t")+name2.count("t")
r=name1.count("r")+name2.count("r")
u=name1.count("u")+name2.count("u")
e=name1.count("e")+name2.count("e")
l=name1.count("l")+name2.count("l")
o=name1.count("o")+name2.count("o")
v=name1.count("v")+name2.count("v")
e=name1.count("e")+name2.count("e")
true=t+r+u+e
love=l+o+v+e
score=int(str(true)+str(love))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
