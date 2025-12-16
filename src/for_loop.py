
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

# print even numbers from 0 to 10 and count the total even numbers
count = 0
for num in range(10, 0, -1):
    if num > 0 and num % 2 == 0:
        print(num)
        count += 1
print("Total even numbers:", count)
