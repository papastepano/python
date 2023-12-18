# Write your solution here
def filter_incorrect():
    correct_lines = []
    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            
            is_correct = True

            # Check if 'week' part is correct
            week_part = parts[0].split(' ')
            if not week_part[1].isdigit():
                is_correct = False
                # raise ValueError("Week number is not an integer!", line)
            
            # Split the numbers
            numbers = parts[1].split(',')
            
            # Check for duplicates 
            numbers = list(set(numbers))

            # check their count
            if len(numbers) != 7:
                is_correct = False

            # Check if all parts are digits and within the correct range
            for num in numbers:
                num = num.strip()
                if not num.isdigit():
                    is_correct = False
                    break
                if int(num) < 1 or int(num) > 39:
                    is_correct = False

            if is_correct:
                correct_lines.append(line + "\n")

    with open("correct_numbers.csv", "w") as file2:
        file2.writelines(correct_lines)

if __name__ == "__main__":
    filter_incorrect()