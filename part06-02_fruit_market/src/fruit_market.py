# write your solution here
def read_fruits():
    with open("fruits.csv") as fruits:
        fruit_dict = {}
        for fruit in fruits:
            fruit = fruit.replace("\n", "")
            parts = fruit.split(";")
            fruit_dict[parts[0]] = float(parts[1])
        return fruit_dict

if __name__ == "__main__":
    read_fruits()