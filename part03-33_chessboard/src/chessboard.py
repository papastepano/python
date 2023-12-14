# Write your solution here
def chessboard(size):
    index = 1
    while index <= size:
        if index % 2 != 0:
            n = 1
            n_arr = []
            while n <= size:
                if n % 2 != 0:
                    n_arr.append("1")
                else:
                    n_arr.append("0")
                n += 1
            print(''.join(map(str, n_arr)))
        else:
            n = 1
            n_arr = []
            while n <= size:
                if n % 2 != 0:
                    n_arr.append("0")
                else:
                    n_arr.append("1")
                n += 1
            print(''.join(map(str, n_arr)))
        index += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
