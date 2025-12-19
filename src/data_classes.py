from collections import namedtuple

# Define a Student data class.
Student = namedtuple("Student", ["name", "age", "grade"])
s1 = Student(name="Udith", age=21, grade="A")
s2 = Student(name="Nimal", age=22, grade="B")

print(f"Student 1: Name: {s1.name}, Age: {s1.age}, Grade: {s1.grade}")
print(f"Student 2: Name: {s2.name}, Age: {s2.age}, Grade: {s2.grade}")
