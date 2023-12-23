import csv
from datetime import datetime, timedelta

def final_points():
    students_start = {}
    final_scores = {}

    with open("start_times.csv") as start_times:
        for line in csv.reader(start_times, delimiter=";"):
            students_start[line[0]] = datetime.strptime(line[1], "%H:%M")

    with open("submissions.csv") as submissions:
        for line in csv.reader(submissions, delimiter=";"):
            student, task, points, submission_time = line
            submission_time = datetime.strptime(submission_time, "%H:%M")

            if submission_time <= students_start[student] + timedelta(hours=3):

                if student not in final_scores:
                    final_scores[student] = {str(i): 0 for i in range(1, 9)}

                task_points = int(points)
                if task_points > final_scores[student][task]:
                    final_scores[student][task] = task_points

    for student in final_scores:
        final_scores[student] = sum(final_scores[student].values())

    return final_scores




if __name__ == "__main__":
    final_points()