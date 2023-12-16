# Write your solution here
diary_file = "diary.txt"
def get_diary_data():
    diary_data = []
    with open(diary_file, "r") as diary:
        for entry in diary:
            entry = entry.replace("\n", "")
            diary_data.append(entry)
    return diary_data

diary_data = get_diary_data()

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_choice = int(input("Function: "))

    if user_choice == 1:
        diary_entry = input("Diary entry: ")
        with open(diary_file, "a") as my_diary:
            my_diary.write(diary_entry + "\n")
            print("Diary saved")
    elif user_choice == 2:
        print("Entries:")
        for entry in diary_data:
            print(entry)
    elif user_choice == 0:
        print("Bye now!")
        break
