# Write your solution here
def new_person(name: str, age: int):
    name_array = name.split(' ')
    if len(name) < 1:
        raise ValueError("Name cannot be empty")
    if len(name_array) < 2:
        raise ValueError("Name must contain at least two words")
    if len(name) < 2 or len(name) > 40:
        raise ValueError("Name must be between 2 and 40 characters")
    if age < 0 or age > 150:
        raise ValueError("Age cannot be negative")
    return (name, age)

if __name__ == "__main__":
    print(new_person('Andrew', 32))