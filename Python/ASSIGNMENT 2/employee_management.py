employees = [
    {"id": 101, "name": "Arun Kumar", "age": 25, "salary": 35000, "department": "IT"},
    {"id": 102, "name": "Priya Sharma", "age": 28, "salary": 42000, "department": "HR"},
    {
        "id": 103,
        "name": "Rahul Raj",
        "age": 30,
        "salary": 55000,
        "department": "Finance",
    },
    {"id": 104, "name": "Sneha Devi", "age": 24, "salary": 38000, "department": "IT"},
    {
        "id": 105,
        "name": "Karthik S",
        "age": 32,
        "salary": 60000,
        "department": "Management",
    },
    {
        "id": 106,
        "name": "Divya Krishnan",
        "age": 27,
        "salary": 45000,
        "department": "Marketing",
    },
    {"id": 107, "name": "Vijay Anand", "age": 29, "salary": 48000, "department": "IT"},
    {"id": 108, "name": "Anjali Menon", "age": 26, "salary": 40000, "department": "HR"},
    {
        "id": 109,
        "name": "Suresh Babu",
        "age": 35,
        "salary": 72000,
        "department": "Finance",
    },
    {
        "id": 110,
        "name": "Meena Raj",
        "age": 31,
        "salary": 58000,
        "department": "Marketing",
    },
    {"id": 111, "name": "Aditya Kumar", "age": 23, "salary": 32000, "department": "IT"},
    {"id": 112, "name": "Pooja Nair", "age": 29, "salary": 47000, "department": "HR"},
    {
        "id": 113,
        "name": "Rohit Sharma",
        "age": 34,
        "salary": 68000,
        "department": "Management",
    },
    {
        "id": 114,
        "name": "Lakshmi Priya",
        "age": 27,
        "salary": 43000,
        "department": "Finance",
    },
    {"id": 115, "name": "Manoj Kumar", "age": 33, "salary": 62000, "department": "IT"},
    {
        "id": 116,
        "name": "Nandhini S",
        "age": 25,
        "salary": 36000,
        "department": "Marketing",
    },
    {"id": 117, "name": "Sanjay Raj", "age": 30, "salary": 51000, "department": "IT"},
    {"id": 118, "name": "Aishwarya R", "age": 28, "salary": 44000, "department": "HR"},
    {
        "id": 119,
        "name": "Gokul Krishna",
        "age": 36,
        "salary": 75000,
        "department": "Finance",
    },
    {
        "id": 120,
        "name": "Harish V",
        "age": 31,
        "salary": 57000,
        "department": "Management",
    },
]

departments = ["Management", "Finance", "HR", "IT", "Marketing"]

total_employee = len(employees)


def get_department(departments: list) -> str:
    print("Choose Department :")
    for i, val in enumerate(departments, start=1):
        print(f"{i}. {val}")
    while True:
        dep_index = int(input("Your Choice :"))
        if dep_index > 0 and dep_index <= len(departments):
            return departments[dep_index - 1]
        else:
            print("Invalid Option")


def get_employee_name() -> str:
    while True:
        employee_name = input("Enter Employee Name : ")
        if employee_name.replace(" ", "").isalpha():
            return employee_name
        else:
            print("Invalid Name")


def get_employee_age() -> int:
    while True:
        employee_age = input("Enter Employee Age : ")
        if employee_age.isdigit() and int(employee_age) >= 18:
            return int(employee_age)
        else:
            print("Invalid Age")


def get_employee_salary() -> float:
    while True:
        employee_salary = float(input("Enter Salary : "))

        if employee_salary > 0:
            return employee_salary
        else:
            print("Invalid Salary")


def add_employee():
    global total_employee
    while True:
        employee_id = int(input("Enter employee ID : "))
        duplicate = False
        for emp in employees:
            if emp["id"] == employee_id:
                duplicate = True
                print("Employee Already Found")
        if not duplicate:
            break

    employee_name = get_employee_name()
    employee_age = get_employee_age()
    employee_salary = get_employee_salary()
    employee_department = get_department(departments)

    data = {
        "id": employee_id,
        "name": employee_name,
        "age": employee_age,
        "salary": employee_salary,
        "department": employee_department,
    }

    employees.append(data)
    total_employee += 1
    print("Employee Added !")


def view_all_employees():
    if not employees:
        print("No Employees Found")
        return

    for i, emp in enumerate(employees, start=1):
        print("=" * 30)
        print(f"{i}.")
        for key, value in emp.items():
            print(f"{key.capitalize()} : {value}")


def search_employees():
    id = int(input("Enter ID to search employee : "))
    for emp in employees:
        if emp["id"] == id:
            view_employee(emp)
            return
    print("No employee found")
    return


def view_employee(emp: dict):
    print("=" * 30)
    print(f"ID : {emp['id']}")
    print(f"Name : {emp['name']}")
    print(f"Age : {emp['age']}")
    print(f"Salary : {emp['salary']}")
    print(f"Department : {emp['department']}")
    print("=" * 30)


def highest_salary(employees: list[dict]):
    if not employees:
        print("No Employees")
    else:
        highest = max(employees, key=lambda emp: emp["salary"])

        view_employee(highest)


def display_employees_by_department():
    if not employees:
        print("No Employees")
        return
    department = input("Enter Department : ")
    found = False
    for emp in employees:
        if emp["department"].lower() == department.lower():
            view_employee(emp)
            found = True
    if not found:
        print("No employee found")


def disp_total_employee_count():
    print(f"Total Employees : {total_employee}")


def disp_department_wise_count(departments: list):
    department_emp_count = {d: 0 for d in departments}
    for emp in employees:
        department_emp_count[emp["department"]] += 1

    for i, (key, val) in enumerate(department_emp_count.items(), start=1):
        print(f"{i}.")
        print(f"{key} - {val}")


def department_wise_highest_salary(departments: list, employees: list[dict]):
    for i, d in enumerate(departments, start=1):
        dept_employees = [x for x in employees if x["department"] == d]
        print(f"{i}. Highest Salary in {d}")
        highest_salary(dept_employees)


def sort_employees_on_salary(employees: list[dict]):
    sorted_employees = sorted(employees, key=lambda emp: emp["salary"])
    for emp in sorted_employees:
        view_employee(emp)


while True:
    print(
        "1. Add Employee\n"
        "2. View Employees \n"
        "3. Search Employee\n"
        "4. Find Highest Salary\n"
        "5. Display Employees by Department\n"
        "6. Total Employee Count\n"
        "7. Department-wise Employee Count\n"
        "8. Department-wise Highest Salary\n"
        "9. Sort Employees based on salary\n"
        "10. Exit"
    )
    option = int(input("Enter a option : "))
    match option:
        case 1:
            add_employee()
        case 2:
            view_all_employees()
        case 3:
            search_employees()
        case 4:
            highest_salary(employees)
        case 5:
            display_employees_by_department()
        case 6:
            disp_total_employee_count()
        case 7:
            disp_department_wise_count(departments)
        case 8:
            department_wise_highest_salary(departments, employees)
        case 9:
            sort_employees_on_salary(employees)
        case 10:
            break
        case _:
            print("Invalid Option")
