# Write your solution here
def spell_out_number(number):
    if 0 <= number < 20:
        return [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ][number]
    elif 20 <= number < 100:
        return [
            "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
        ][number // 10] + ("-" + spell_out_number(number % 10) if number % 10 != 0 else "")
    else:
        return "out of range"

def dict_of_numbers():
    return {i: spell_out_number(i) for i in range(100)}


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    # print(numbers[45])
    # print(numbers[99])
    # print(numbers[0])