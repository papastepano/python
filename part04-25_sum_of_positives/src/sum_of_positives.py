# Write your solution here
def sum_of_positives(nums):
    return sum(x for x in nums if x > 0)

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)