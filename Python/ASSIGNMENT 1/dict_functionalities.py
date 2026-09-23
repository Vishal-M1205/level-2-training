person = {"name": "John", "age": 25, "city": "Chennai"}
print("Original:", person)

print("Name:", person["name"])
print("Get age:", person.get("age"))
print("Get gender with default:", person.get("gender", "Not Specified"))

person["salary"] = 50000
print("After adding salary:", person)

person["age"] = 26
print("After updating age:", person)

person.update({"city": "Coimbatore", "dept": "IT"})
print("After update:", person)

print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

removed_salary = person.pop("salary")
print("Popped salary:", removed_salary)
print("After pop:", person)

last_item = person.popitem()
print("Popped item:", last_item)
print("After popitem:", person)

del person["city"]
print("After del:", person)

print("Is 'name' in dict:", "name" in person)
print("Length:", len(person))

copy_dict = person.copy()
print("Copied:", copy_dict)

squares = {x: x * x for x in range(1, 6)}
print("Dict comprehension:", squares)

person.clear()
print("After clear:", person)
