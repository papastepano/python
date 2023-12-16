# Write your solution here
def calculate_expression(expression):
    if '+' in expression:
        numbers = expression.split('+')
        return int(numbers[0]) + int(numbers[1])
    elif '-' in expression:
        numbers = expression.split('-')
        return int(numbers[0]) - int(numbers[1])
    else:
        raise ValueError("Unsupported operation")
    
def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv", "r") as solutions:
        for solution in solutions:
            student = {}
            solution = solution.replace("\n", "")
            parts = solution.split(";")

            student["name"] = parts[0]
            student["problem"] = parts[1]
            student["result"] = int(parts[2])

            solution = calculate_expression(student["problem"])

            if student["result"] == solution:
                correct.append(student)
            else:
                incorrect.append(student)

    with open("correct.csv", "w") as correct_file:
        for student in correct:
            correct_file.write(f"{student['name']};{student['problem']};{student['result']}\n")
    
    with open("incorrect.csv", "w") as incorrect_file:
        for student in incorrect:
            incorrect_file.write(f"{student['name']};{student['problem']};{student['result']}\n")

if __name__ == "__main__":
    filter_solutions()