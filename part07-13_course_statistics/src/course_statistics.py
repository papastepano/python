# Write your solution here
import urllib.request
import json
import math

def retrieve_all() -> list[tuple]:
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    courses = []
    for course in data:
        # retrieve_course(course["name"])
        
        if course["enabled"] != False:
            courses.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
    return courses

def retrieve_course(course_name: str):
    statistics = {}
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    weeks = 0
    students = 0
    hours = 0
    exercises = 0

    for week, info in data.items():
        hours += info["hour_total"]
        exercises += info["exercise_total"]
        
        if info["students"] > students:
            students = info["students"]
        weeks += 1

    statistics["weeks"] = weeks
    statistics["students"] = students
    statistics["hours"] = hours
    if students > 0:
        statistics["hours_average"] = math.floor(hours / students)
    else:
        statistics["hours_average"] = 0 

    statistics["exercises"] = exercises
    
    if students > 0:
        statistics["exercises_average"] = math.floor(exercises / students)
    else:
        statistics["exercises_average"] = 0 


    return statistics

if __name__ == "__main__":
    # courses = retrieve_all()
    # retrieve_course("docker2019")
    # retrieve_course("ohtus17")
    # retrieve_course("ofs")
    # retrieve_course("ohtu2018")
    # retrieve_course("docker-beta")
    # retrieve_course("rails2018")
    # retrieve_course("docker18")
    # retrieve_course("fullstack2019")
    retrieve_course("CCFUN")
    # retrieve_course("ofs2019")
    # retrieve_course("docker2020")
    # retrieve_course("beta-dwk-2020")
    # retrieve_course("fullstack2020")