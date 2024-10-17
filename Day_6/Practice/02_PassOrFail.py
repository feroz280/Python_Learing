#write a program to find out whether a student has passed or failed if it requires a totoal of 40% and at least 33% in each subject to pass. Assume 3 subjects and takke marks as an unput from the user.

marks_1 = int(input("Enter marks of first subject :"))
marks_2 = int(input("Enter marks of seconnd subject :"))
marks_3 = int(input("Enter marks of third subject :"))
total_marks = 300
sum_of_marks = marks_1 + marks_2 + marks_3
# print(sum_of_marks)
if((sum_of_marks / total_marks)*100 >= 44):
    print("Conngrats ...!! Your are pass...")
elif((sum_of_marks / total_marks) * 100 >= 33) :
    print("Your are pass...!!")
else:
    print("You need more hardwork , Try Again...!!")
