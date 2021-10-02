#who pay
"""This program chooses a participant among all participents randomly, and that
person will pay the bill for all persons."""
names=input("Write the names of the participants with a comma and a <space> between\nthe names.\n")
names=names.split(", ")
import random
name_length=len(names)
random_number=random.randint(0,name_length-1)
random_name=names[random_number]
print(f"{random_name} will pay the bill for everyone.")
