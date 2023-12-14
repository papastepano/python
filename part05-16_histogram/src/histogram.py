# Write your solution here
def histogram(my_string: str):
    histogram = {}
    for i in my_string:
        if i not in histogram:
            histogram[i] = ""
        histogram[i] = histogram[i] + '*'
    
    for key, value in histogram.items():
        print(f"{key} {value}")

if __name__ == "__main__":
    histogram("statistically")