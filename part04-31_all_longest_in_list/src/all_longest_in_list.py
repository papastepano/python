# Write your solution here
def all_the_longest(my_list: [str]):
    max_length = max(len(s) for s in my_list)
    return [s for s in my_list if len(s) == max_length]


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']