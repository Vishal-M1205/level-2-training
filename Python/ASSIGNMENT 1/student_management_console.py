students = []


def addStudent():
    name = input("Enter your name : ")

    while True:
        roll_no = int(input("Enter Roll Number: "))
        dup_rollno = False
        for st in students:
            if st["rollno"] == roll_no:
                print("User Already Found")
                dup_rollno = True
                break
        if dup_rollno:
            pass
        else:
            break
    while True:
        mark = int(input("Enter Mark : "))
        if mark >= 0 and mark <= 500:
            break
        else:
            print("Invalid Mark")
    students.append({"name": name, "rollno": roll_no, "mark": mark})


def viewStudent():
    if not students:
        print("No Students")
        return
    for i, st in enumerate(students, start=1):
        print(i)
        for key, value in st.items():
            print(f"{key} : {value}")


def searchStudent():
    if not students:
        print("No Students")
        return

    roll_no = int(input("Enter Rollno : "))
    for st in students:
        if st["rollno"] == roll_no:
            for key, value in st.items():
                print(f"{key} : {value}")
            return
    print("No student found")
    return


def calculateAverage():
    total = 0
    for st in students:
        total += st["mark"]
    print(f"Average : {total/len(students)}")


def getTopperStudent():
    if not students:
        print("No Students")
        return

    top = students[0]

    for st in students:
        if top["mark"] < st["mark"]:
            top = st
    for key, value in top.items():
        print(f"{key} : {value}")


def dispPassedStudents():
    if not students:
        print("No Students")
        return

    passed = [st for st in students if st["mark"] >= 350]

    if not passed:
        print("No Student Passed")
        return

    for st in passed:
        for key, value in st.items():
            print(f"{key} : {value}")


while True:
    print(
        "1. Add Student\n"
        "2. View Students\n"
        "3. Search Student\n"
        "4. Calculate Average\n"
        "5. Find Topper\n"
        "6. Display Passed Students\n"
        "7. Exit\n"
    )

    option = int(input("Choose a option : "))

    match option:
        case 1:
            addStudent()
        case 2:
            viewStudent()
        case 3:
            searchStudent()
        case 4:
            calculateAverage()
        case 5:
            getTopperStudent()
        case 6:
            dispPassedStudents()
        case _:
            break
