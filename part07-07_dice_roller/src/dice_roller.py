# Write your solution here
import random

def roll(die: str):
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]
    for i in die:
        if i == "A":
            return random.choice(A)
        elif i == "B":
            return random.choice(B)
        elif i == "C":
            return random.choice(C)

def play(die1: str, die2: str, times: int) -> tuple:
    one_wins = 0
    two_wins = 0
    ties = 0
    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            one_wins += 1
        elif roll1 < roll2:
            two_wins += 1
        else:
            ties += 1
    return (one_wins, two_wins, ties)

if __name__ == "__main__":
    # for i in range(20):
    #     print(roll("A"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("B"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("C"), " ", end="")

    result = play("A", "B", 100)
    print(result)
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)