import csv
from datetime import datetime, timedelta

def cheaters():
    all_students = {}
    cheaters = []

    with open("start_times.csv") as start_times:
        for line in csv.reader(start_times, delimiter=";"):
            all_students[line[0]] = {}
            all_students[line[0]]["start"] = datetime.strptime(line[1], "%H:%M")
            all_students[line[0]]["excercises"] = []
            all_students[line[0]]["latest_submission"] = datetime.strptime("00:00", "%H:%M")

    with open("submissions.csv") as submissions:
        for line in csv.reader(submissions, delimiter=";"):
            excercise = {"excercise": line[1], "points": int(line[2]), "end": datetime.strptime(line[3], "%H:%M")}
            all_students[line[0]]["excercises"].append(excercise)
            if excercise["end"] > all_students[line[0]]["latest_submission"]:
                all_students[line[0]]["latest_submission"] = excercise["end"]

    for key, value in all_students.items():
        time_spent = value["latest_submission"] - value["start"]
        if time_spent > timedelta(hours=3):
            cheaters.append(key)

    return cheaters

if __name__ == "__main__":
    cheaters()