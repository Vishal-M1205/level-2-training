import math

print("Stuent Analyzer")

student_name = input("Enter Student Name : ")

subjects = ["Tamil", "English", "Science", "Maths", "Computer"]

marks = {}

for s in subjects:
    while True:
        mark = int(input(f"Enter {s} Mark : "))
        if mark >= 0 and mark <= 100:
            marks[s] = mark
            break
        else:
            print("Invalid Mark : mark should be less than 100, greater than 0 ")


total_marks = sum(marks.values())
average_mark = sum(marks.values()) / len(marks)

grade = ""

match total_marks:
    case total_marks if total_marks >= 90:
        grade = "A"
    case total_marks if total_marks >= 70:
        grade = "B"
    case total_marks if total_marks >= 50:
        grade = "C"
    case _:
        grade = "F"

exam_result = "PASS" if total_marks >= 50 else "FAIL"

print(f"Student Name: {student_name}")

for key, value in marks.items():
    print(f"{key} : {value}")
print(f"Total : {total_marks}")
print(f"Average : {average_mark}")
print(f"Grade : {grade}")
print(f"Result : {exam_result}")
