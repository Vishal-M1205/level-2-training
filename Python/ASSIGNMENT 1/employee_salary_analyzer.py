employee_name = input("Enter Employee Name : ")

while True:
    basic_salary = int(input("Enter Basic Salary : "))
    if basic_salary > 0:
        break
    else:
        print("Invalid Basic Salary Amount")

while True:
    employee_experience = int(input("Enter Experience : "))
    if employee_experience >= 0:
        break
    else:
        print("Invalid Experience")


hra_amount = basic_salary * 0.18
da_amount = basic_salary * 0.12

bonus = 0

if employee_experience >= 5:
    bonus = 5000
elif employee_experience >= 2:
    bonus = 1000

gross_salary = hra_amount + da_amount + bonus + basic_salary

final_salary_category = ""

match gross_salary:
    case gross_salary if gross_salary >= 100000:
        final_salary_category = "High"
    case gross_salary if gross_salary >= 50000:
        final_salary_category = "Medium"
    case _:
        final_salary_category = "Low"

print(f"Employee Name : {employee_name}")
print(f"Employee Experience : {employee_experience}")
print(f"Basic Salary : {basic_salary}")
print(f"HRA : {hra_amount}")
print(f"DA : {da_amount}")
print(f"Bonus : {bonus}")
print(f"Gross Salary : {gross_salary}")
print(f"Category : {final_salary_category}")
