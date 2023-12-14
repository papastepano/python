# Write your solution here
def create_tuple(x: int, y: int, z: int):
    truple = (x,y,z)
    smallest = min(truple)
    greatest = max(truple)
    truple_sum = sum(truple)
    return (smallest, greatest, truple_sum)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1)) 