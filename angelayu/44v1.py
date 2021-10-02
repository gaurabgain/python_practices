#44 rock-paper-scissor v1
#rough works
import random
print("Welcome to rock-paper-scissors game.")
choices=["Rock","Paper","Scissors"]
user_input=int(input("Choose\n0 for Rock\n1 for Paper\n2 for Scissors\n"))
if user_input==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif user_input==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif user_input==2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print(f"Your choice: {choices[user_input]}")
computer_input=random.randint(0,2)
if computer_input==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computer_input==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif computer_input==2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print(f"Computer choice: {choices[computer_input]}")
if user_input==0 and computer_input==1:
    print("You lose")
elif user_input==0 and computer_input==2:
    print("You Win")
elif user_input==1 and computer_input==0:
    print("You Win")	
elif user_input==1 and computer_input==2:
    print("You lose")
elif user_input==2 and computer_input==0:
    print("You lose")
elif user_input==2 and computer_input==1:
    print("You win")
else:
    print("It is a draw.")
