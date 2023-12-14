# Write your solution here
def even_numbers(numbers: []) -> []:
    to_return = []
    for n in numbers:
        if n %2 == 0:
            to_return.append(n)

    return to_return