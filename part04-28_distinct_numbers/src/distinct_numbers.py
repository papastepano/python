# Write your solution here
def distinct_numbers(the_list: [int]) -> [int]:
    new_list = []
    the_list.sort()
    for n in the_list:
        if n not in new_list:
            new_list.append(n)
    return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
