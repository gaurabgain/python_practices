#program to calculate average height
student_heights=input("input a list of student heights in centimeter\n").split()
n=0
total_height=0
for height in student_heights:
    height=int(student_heights[n])
    total_height+=height
    n+=1
print(f"Sum of height of students is {total_height} .")
print(f"Total number of students is {n} .")
av_height=round(total_height/n,2)
print(f"Average height of students heights in centimeters is {av_height} .")
