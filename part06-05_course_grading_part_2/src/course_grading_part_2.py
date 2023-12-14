# wite your solution here
def calculate_exercise_points(completed_exercises, total_exercises):
    completion_percentage = (completed_exercises / total_exercises) * 100

    if completion_percentage >= 10:
        points = completion_percentage // 10
    else:
        points = 0

    return min(int(points), 10)

def calculate_grade(exam_points, completed_exercises, total_exercises):
    exercise_points = calculate_exercise_points(completed_exercises, total_exercises)
    total_points = exam_points + exercise_points

    if total_points >= 0 and total_points <= 14:
        return 0
    elif total_points >= 15 and total_points <= 17:
        return 1
    elif total_points >= 18 and total_points <= 20:
        return 2
    elif total_points >= 21 and total_points <= 23:
        return 3
    elif total_points >= 24 and total_points <= 27:
        return 4
    else:
        return 5

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

combined_data = {}

with open(student_info) as student_info:
    index = 0
    for s in student_info:
        if index:
            s = s.replace("\n", "")
            parts = s.split(";")
            combined_data[parts[0]] = {}
            combined_data[parts[0]]["first_name"] = parts[1]
            combined_data[parts[0]]["last_name"] = parts[2]
            combined_data[parts[0]]["exercise_data"] = []
            combined_data[parts[0]]["exam_data"] = []
        index += 1


with open(exercise_data) as exercise_data:
    index = 0
    for e in exercise_data:
        if index:
            e = e.replace("\n", "")
            parts = e.split(";")
            exercise_data = [int(x) for x in parts[1:]]
            combined_data[parts[0]]["exercise_data"].extend(exercise_data)
            combined_data[parts[0]]["exercise_total"] = sum(combined_data[parts[0]]["exercise_data"])
        index += 1


with open(exam_points) as exam_points:
    index = 0
    for e in exam_points:
        if index:
            e = e.replace("\n", "")
            parts = e.split(";")
            exam_data = [int(x) for x in parts[1:]]
            combined_data[parts[0]]["exam_data"].extend(exam_data)
            combined_data[parts[0]]["exam_total"] = sum(combined_data[parts[0]]["exam_data"])
        index += 1

for student in combined_data:
    completed_exercises = combined_data[student]["exercise_total"]
    total_exercises = 40

    grade = calculate_grade(combined_data[student]["exam_total"], completed_exercises, total_exercises)
    print(combined_data[student]["first_name"], combined_data[student]["last_name"], grade)

# jaana javanainen 27 11 