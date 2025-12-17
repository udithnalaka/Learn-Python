numbers_list = [1, 2, 3, 4, 5, 1]
numbers_1 = set(numbers_list)
print("Unique numbers:", numbers_1)

numbers_2 = {4, 5, 6, 7}
numbers_2.add(8)
print("Numbers 2 after add:", numbers_2)
numbers_2.remove(5)
print("Numbers 2 after remove:", numbers_2)
numbers_2.update([9, 10, 11, 1])
print("Numbers 2 after update:", numbers_2)

print(numbers_1 | numbers_2)  # union
print(numbers_1 & numbers_2)  # intersection

# This will raise a TypeError because sets are unordered and do not support indexing
# print(numbers_1[1])
