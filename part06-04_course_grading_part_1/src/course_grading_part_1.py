# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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

for student in combined_data:
    print(combined_data[student]["first_name"], combined_data[student]["last_name"], combined_data[student]["exercise_total"] )