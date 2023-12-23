# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = json.load(file)
        for person in data:
            print(f"{person['name']} {person['age']} years ({', '.join(person['hobbies'])})")
            
if __name__ == "__main__":
    print_persons("file1.json")