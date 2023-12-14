# Write your solution here
def seven_brothers():
    names = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
    sorted_names = sorted(names)
    for name in sorted_names:
        print(name)
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
  seven_brothers()