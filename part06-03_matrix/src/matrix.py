# write your solution here
def matrix_sum():
    with open("matrix.txt") as matrix:
        new_matrix = []
        for m in matrix:
            m = m.replace("\n", "")
            parts = m.split(",")
            for item in parts:
                new_matrix.append(int(item))
        return sum(new_matrix)

def matrix_max():
    with open("matrix.txt") as matrix:
        new_matrix = []
        for m in matrix:
            m = m.replace("\n", "")
            parts = m.split(",")
            for item in parts:
                new_matrix.append(int(item))
        return max(new_matrix)


def row_sums():
    with open("matrix.txt") as matrix:
        new_matrix = []
        for m in matrix:
            m = m.replace("\n", "")
            parts = m.split(",")
            nums = [int(n) for n in parts]
            new_matrix.append(sum(nums))
        return new_matrix


if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()