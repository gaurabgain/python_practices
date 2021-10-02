#this program finds the higest number in a list.
scores=input("Write the scores :\n").split()
highest_score=0
for score in scores:
    score=int(score)
    #print(type(score))
    if score>highest_score:
        highest_score=score
print(f"The score values are: {scores}")
print(f"The highest score is: {highest_score}")
