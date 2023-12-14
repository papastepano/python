# Write your solution here
def shortest(my_list: [str]):
    return min(my_list, key=len)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)
