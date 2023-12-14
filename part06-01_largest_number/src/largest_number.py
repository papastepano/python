# write your solution here

def largest():
    with open("numbers.txt") as numbers:
        # for line in numbers:
        #     line = line.replace("\n", "")
        #     print(line)

        nums = [int(n) for n in numbers]
        return max(nums)

if __name__ == "__main__":
    largest()