# Write your solution here
def print_letter_square(layers):
    if layers > 26:
        print("Error: Too many layers. Maximum allowed is 26.")
        return

    size = 2 * layers - 1
    mid = size // 2

    for i in range(size):
        row = ""
        for j in range(size):
            distance = max(abs(i - mid), abs(j - mid))
            letter = chr(ord('A') + min(distance, layers - 1))
            row += letter
        print(row)

layers = int(input("Layers: "))
print_letter_square(layers)