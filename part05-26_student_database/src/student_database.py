# Write your solution here
def add_student(students: dict, name: str):
    students[name] = {}
    students[name]["average"] = 0

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        if 'courses' not in students[name] or len(students[name]['courses']) == 0:
            print(" no completed courses")
        else:
            total_grade = 0
            print(f" {len(students[name]['courses'])} completed courses:")
            for c in students[name]['courses']:
                print(f"  {c[0]} {c[1]}")
                total_grade += c[1]
            if students[name]['average']:
                print(f" average grade {students[name]['average']}")

def add_course(students: dict, name: str, course_info: tuple):
    if 'courses' not in students[name]:
        students[name]['courses'] = []

    if course_info[0] not in students[name]['courses'] and course_info[1] != 0:
        add_new_course = True
        course_index = 0
        for course in students[name]['courses']:
            if course_info[0] == course[0]:
                # mark for adding
                if course_info[1] < course[1]:
                    add_new_course = False
                    break
                # replace with higher grade
                if course_info[1] > course[1]:
                    students[name]['courses'][course_index] = course_info
                    add_new_course = False
                    calc_average(students, name)
            course_index += 1
        if add_new_course:
            students[name]['courses'].append(course_info)
            calc_average(students, name)

def calc_average(students: dict, name: str):
    total_grade = 0
    for c in students[name]['courses']:
        total_grade += c[1]
    
    students[name]["average"] = total_grade / len(students[name]['courses'])

def summary(students: dict):
    print(f"students {len(students)}")
    all_average = []
    course_count = []
    for key, value in students.items():
        all_average.append((key, value["average"]))
        course_count.append((key, len(value["courses"])))
    best_average = all_average[0]
    most_courses = course_count[0]
    for best in all_average[1:]:
        if best[1] > best_average[1]:
            best_average = best
    for most in course_count[1:]:
        if most[1] > most_courses[1]:
            most_courses = most

    print(f"most courses completed {most_courses[1]} {most_courses[0]}")
    print(f"best average grade {best_average[1]} {best_average[0]}")



if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")