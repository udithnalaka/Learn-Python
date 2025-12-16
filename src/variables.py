
print("Learn about variables in Python!")

first_name = "Udith"
last_name = "Rassapana"
student_age = 21
is_international = True
rating = 4.5
cource_name = "Python Programming"
full_name = f"{first_name} {last_name}"

print("Student Name:", first_name)
print("Student Age:", student_age)
print("Is International Student:", is_international)
print("Course Rating:", rating)
print("Course Name:", cource_name)
print(f"My full name: {full_name}")

print(len(first_name))
print(cource_name[2])
print(cource_name[0:6])
print(cource_name[-2])

print(full_name.upper())
print(full_name.lower())
print(cource_name.strip())  # remove white spaces
print(cource_name.replace("Python", "Java"))
print(cource_name.find("Py"))  # find the index of substring
print("python" in cource_name)
print("Python" in cource_name)
print("Java" not in cource_name)
