# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    matching = 0
    for m in my_matrix:
        for n in m:
            if n == element:
                matching += 1
            
    return matching

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    g = [[1, 5, 5, 3], [2, 5, 2, 5], [0, 0, 2, 5]]
    print(count_matching_elements(g, 1))