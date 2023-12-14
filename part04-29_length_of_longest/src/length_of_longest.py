# Write your solution here
def length_of_longest(my_list: [str]):
    return max(len(s) for s in my_list)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)