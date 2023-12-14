# Write your solution here
def factorials(n: int):
    factorial = {}
    for j in range(1,n+1):
        if j > 1:
            factorial[j] = factorial[j - 1] * j
        else:
            factorial[1] = 1

    return factorial

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])

    # 1
    # 6
    # 120