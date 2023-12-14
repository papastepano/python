# Write your solution here
def everything_reversed(input_list):
    reversed_strings = [s[::-1] for s in input_list]
    return reversed_strings[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)