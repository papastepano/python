# Write your solution here
items = int(input("How many items: "))
values = []
i = 0

while i < items:
    value = int(input(f"Item {i + 1}: "))
    values.append(value)
    i += 1

print(values)