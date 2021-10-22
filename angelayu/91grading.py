'''
concepts used
dictionary
if/else statements
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
"""
grading criteria-
    Scores 91 - 100: Grade = "Outstanding"

    Scores 81 - 90: Grade = "Exceeds Expectations"

    Scores 71 - 80: Grade = "Acceptable"

    Scores 70 or lower: Grade = "Fail"
"""
#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for names in student_scores:
    marks = student_scores[names]
    if marks >=91 and marks <=100:
        student_grades[names]="Outstanding"
    elif marks >=81 and marks<=90:
        student_grades[names]="Exceeds Expectations"
    elif marks>=71 and marks<=80:
        student_grades[names]="Acceptable"
    elif marks<=70:
        student_grades[names]="Fail"
# 🚨 Don't change the code below 👇
print(student_grades)
