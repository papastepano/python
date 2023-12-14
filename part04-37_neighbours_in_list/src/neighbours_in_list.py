# Write your solution here
def longest_series_of_neighbours(input_list: []):
    longest_streak = 1
    current_streak = 1

    for i in range(1, len(input_list)):
        if abs(input_list[i] - input_list[i - 1]) == 1:
            current_streak += 1
        else:
            current_streak = 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak