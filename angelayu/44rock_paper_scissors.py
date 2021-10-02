#rock,paper,scissors game.
import random
print("Welcome to rock-paper-scissors game.")
you=int(input("Choose one of these\n0 for Rock\n1 for Paper\n2 for Scissors\nYour choice : "))
choices=["Rock","Paper","Scissors"]
win="You win!"
lose="You lost"
if you==0:
    print( '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif you==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif you==2:
    print( '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("You have entered wrong entries. Please try again.")
print(f"You have choosen {choices[you]}.")
comp_choice=random.randint(0,2)
if comp_choice==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif comp_choice==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif comp_choice==2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print(f"Computer has choosen {choices[comp_choice]}.")
if you==0 and comp_choice==1:
    print("You lost")
elif you==0 and comp_choice==2:
    print("You win!")
elif you==1 and comp_choice==0:
    print("You win!")
elif you==1 and comp_choice==2:
    print("You lose")
elif you==2 and comp_choice==0:
    print("You lose")
elif you==2 and comp_choice==1:
    print("You win!")
elif you==comp_choice:
    print("It is a draw.")
