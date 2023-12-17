# tee ratkaisu tänne
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
    course_info = input("Course information: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_info = "course1.txt"

combined_data = {}
header_text = ""

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

with open(course_info, "r") as course_information:
    for line in course_information:
        line = line.replace("\n", "")
        parts = line.split(":")
        if parts[0] == "name":
            header_text += f"{parts[1].strip()}, "
        elif parts[0] == "study credits":
            header_text += f"{parts[1].strip()} credits\n"
        else:
            raise ValueError("Invalid course information")
    header_length = len(header_text) - 1
    header_text = header_text + "=" * header_length + "\n"

def write_to_txt(combined_data):
    with open("results.txt", "w") as results:
        results.write(header_text)
        results.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
        results.write("\n")
        for student in combined_data:
            full_name = combined_data[student]["first_name"] + ' ' + combined_data[student]["last_name"]
            total_exercises = 40
            excercise_points = calculate_exercise_points(combined_data[student]["exercise_total"], total_exercises)
            completed_exercises = combined_data[student]["exercise_total"]
            grade = calculate_grade(combined_data[student]["exam_total"], completed_exercises, total_exercises)
            results.write(f"{full_name:30}{str(combined_data[student]['exercise_total']):10}{str(excercise_points):10}{str(combined_data[student]['exam_total']):10}{str(combined_data[student]['exam_total'] + excercise_points):10}{str(grade):10}")
            results.write("\n")


def write_to_csv(combined_data):
    with open("results.csv", "w") as results:
        for key,value in combined_data.items():
            grade = calculate_grade(value["exam_total"], value["exercise_total"], 40)
            results.write(f"{key};{value['first_name']} {value['last_name']};{grade}\n")

write_to_txt(combined_data)
write_to_csv(combined_data)

print("Results written to files results.txt and results.csv")