point = {"x": 1, "y": 2}
print("X coordinate:", point["x"])

point_1 = dict(x=10, y=20)
print("Y coordinate:", point_1["y"])

# print("Unavailable key", point["z"]) # will raise KeyError
print("Unavailable key", point.get("z", 0))  # default value if key not found

# unpacking dictionary
combined_point = {**point, **point_1, "a": 5}
print("Combined Point:", combined_point)

# print with key
for key in point:
    print(f"Key: {key}, Value: {point[key]}")

# print key and value
for key, value in point.items():
    print(f"Key: {key}, Value: {value}")

# print with items(). will print as tuples.
for item in point.items():
    print(f"Item: {item}")

# dictionary of User objects and print user information
user_dict = {
    1: {"id": 1, "name": "Udith", "age": 21},
    2: {"id": 2, "name": "Nimal", "age": 22},
    3: {"id": 3, "name": "Kamal", "age": 23}
}
print("\nUser information")
for user_id, user_info in user_dict.items():
    print(
        f"User ID: {user_id}, Name: {user_info['name']}, Age: {user_info['age']}")
