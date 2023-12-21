# Write your solution here
from datetime import datetime, timedelta

total_minutes = 0
average_minutes = 0
all_days = {}

user_filename = input("Filename: ")
user_start_date = datetime.strptime(input("Start date: "), "%d.%m.%Y")
user_days = int(input("How many days: "))
for i in range(user_days):
    next_day = user_start_date + timedelta(days=i)
    current_day = next_day.strftime("%d.%m.%Y") 
    user_day = input(f"Screen time {current_day}: ")
    user_day = user_day.split(" ")
    user_day = [int(i) for i in user_day]
    total_minutes += sum(user_day)
    average_minutes = total_minutes / (i + 1)

    all_days[current_day] = user_day

with open(user_filename, "w") as file:
    formated_date = user_start_date.strftime("%d.%m.%Y")
    file.write(f"Time period: {formated_date}-{list(all_days.keys())[-1]}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {average_minutes}\n")
    
    for day, time in all_days.items():
        file.write(f"{day}: {"/".join(str(i) for i in time)}\n")
print(f"Data stored in file {user_filename}")
