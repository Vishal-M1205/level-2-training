employees = []


def addEmployee():
    while True:
        id = int(input("Enter employee ID : "))
        for emp in employees:
            if emp["id"] == id:
                print("Employee Already Found")
        employee_name = input("Enter Employee Name : ")
        employee_age = int(input("Enter Employee Age : "))
        employee_salary = float(input("Enter Salary : "))
        department = input("Enter Department : ")

        data = {
            "id": id,
            "name": employee_name,
            "age": employee_age,
            "salary": employee_salary,
            "department": department,
        }

        employees.append(data)
        print("Employee Added !")
        break


def viewEmployees():
    if not employees:
        print("No Employees Found")
        return

    for emp in employees:
        print(f"ID : {emp['id']}")
        print(f"Name : {emp['name']}")
        print(f"Age : {emp['age']}")
        print(f"Salary : {emp['salary']}")
        print(f"Department : {emp['department']}")


def searchEmployees():
    id = int(input("Enter ID to search employee : "))
    for emp in employees:
        if emp["id"] == id:
            print(f"ID : {emp['id']}")
            print(f"Name : {emp['name']}")
            print(f"Age : {emp['age']}")
            print(f"Salary : {emp['salary']}")
            print(f"Department : {emp['department']}")
            return
    print("No employee found")
    return


def highestSalary():
    if not employees:
        print("No Employees")
    else:
        highest = employees[0]

        for emp in employees:
            if highest["salary"] < emp["salary"]:
                highest = emp
        print(f"ID : {highest['id']}")
        print(f"Name : {highest['name']}")
        print(f"Age : {highest['age']}")
        print(f"Salary : {highest['salary']}")
        print(f"Department : {highest['department']}")


def displayEmployeesByDepartment():
    if not employees:
        print("No Employees")
        return
    department = input("Enter Department : ")
    found = False
    for emp in employees:
        if emp["department"].lower() == department.lower():
            print(f"ID : {emp['id']}")
            print(f"Name : {emp['name']}")
            print(f"Age : {emp['age']}")
            print(f"Salary : {emp['salary']}")
            print(f"Department : {emp['department']}")
            found = True
    if not found:
        print("No employee found")


while True:
    print(
        "1. Add Employee\n"
        "2. View Employees \n"
        "3. Search Employee\n"
        "4. Find Highest Salary\n"
        "5. Display Employees by Department\n"
        "6. Exit "
    )
    option = int(input("Enter a option : "))
    match option:
        case 1:
            addEmployee()
        case 2:
            viewEmployees()
        case 3:
            searchEmployees()
        case 4:
            highestSalary()
        case 5:
            displayEmployeesByDepartment()
        case 6:
            break
        case _:
            print("Invalid Option")
