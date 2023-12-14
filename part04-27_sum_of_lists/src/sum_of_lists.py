# Write your solution here
def list_sum(list1: [int], list2: [int]):
    new_list = []
    for n in range(0, len(list1)):
        new_list.append(list1[n] + list2[n])

    return new_list


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]