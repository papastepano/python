# Write your solution here
exam_points_list = []
exercise_points_list = []
grade_list = []

def word_split(sentence):
    return sentence.split()

def calculate_exercise_points(exercise_completed):
    return min(exercise_completed // 10, 10)

def process():
    print("Statistics:")
    
    points_average = (sum(exam_points_list) + sum(exercise_points_list)) / len(exam_points_list)
    pass_percentage = (sum(grade > 0 for grade in grade_list) / len(grade_list)) * 100

    print("Points average:", round(points_average,1))
    print("Pass percentage:", round(pass_percentage,1))
    print("Grade distribution: ")
    print(" 5:", grade_list.count(5)*"*")
    print(" 4:", grade_list.count(4)*"*")
    print(" 3:", grade_list.count(3)*"*")
    print(" 2:", grade_list.count(2)*"*")
    print(" 1:", grade_list.count(1)*"*")
    print(" 0:", grade_list.count(0)*"*")

def calculate_grade(exam_points, exercise_points):
    total_points = exam_points + exercise_points
    if exam_points < 10:
        return 0
    elif total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    elif total_points <= 30:
        return 5
    else:
        return -1

while True:
    user_input = input("Exam points and exercises completed: ")
    
    if not user_input:
        process()
        break

    exam_points = int(word_split(user_input)[0])
    exercise_points = int(word_split(user_input)[1])

    if exam_points not in range(0,21) or exercise_points not in range(0,101):
        break

    exercise_points_list.append(calculate_exercise_points(exercise_points))
    exam_points_list.append(exam_points)
    grade_list.append(calculate_grade(exam_points, calculate_exercise_points(exercise_points)))


