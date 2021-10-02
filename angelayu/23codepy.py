#to calculate number of days,weeks,months,years left if i lived for 90 years.
current_age = int(input("How old are you?\n"))
age_left= 90-current_age
days=365*age_left
weeks=52*age_left
months=12*age_left
print(f"You have\n{days} days or\n{weeks} weeks or\n{months} months or\n{age_left} years left.")
