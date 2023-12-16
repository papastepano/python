# Write your solution here
sign_to = input("Whom should I sign this to: ")
save_to = input("Where shall I save it: ")

with open(save_to, "w") as my_file:
    my_file.write(f"Hi {sign_to}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")