students = [
    ("Udith", 25),
    ("Nimal", 22),
    ("Kamal", 23),
]


# lambda functions
# Map function
age_map = map(lambda student: student[1], students)
print("Student age", list(age_map))

# Filter function
age_filter = filter(lambda student: student[1] > 22, students)
print("Students older than 22:", list(age_filter))
