# Write your solution here
def run(program):
    # Initialize variables A to Z with value 0
    variables = {chr(i): 0 for i in range(65, 91)}

    # Function to evaluate a value - it could be a direct integer or a variable
    def evaluate_value(value):
        try:
            # If it's a direct integer
            return int(value)
        except ValueError:
            # If it's a variable
            return variables[value]

    # Store the locations of labels for jumping
    labels = {}
    for i, line in enumerate(program):
        if ":" in line and "::" not in line:
            label_name = line.replace(":", "")
            labels[label_name] = i 

    # List to store the results of PRINT commands
    output = []

    # Start executing the program
    pc = 0  # Program counter
    while pc < len(program):
        line = program[pc].split()
        command = line[0]

        # Process the command
        if command == "PRINT":
            output.append(evaluate_value(line[1]))
        elif command == "MOV":
            variables[line[1]] = evaluate_value(line[2])
        elif command == "ADD":
            variables[line[1]] += evaluate_value(line[2])
        elif command == "SUB":
            variables[line[1]] -= evaluate_value(line[2])
        elif command == "MUL":
            variables[line[1]] *= evaluate_value(line[2])
        elif command == "JUMP":
            pc = labels[line[1]]
            continue
        elif command == "IF":
            # Extract the condition and evaluate it
            left, comparison, right, _, jump_label = line[1:6]
            left_val = evaluate_value(left)
            right_val = evaluate_value(right)

            # Check the condition and perform jump if true
            condition_met = False
            if comparison == "==":
                condition_met = left_val == right_val
            elif comparison == "!=":
                condition_met = left_val != right_val
            elif comparison == "<":
                condition_met = left_val < right_val
            elif comparison == "<=":
                condition_met = left_val <= right_val
            elif comparison == ">":
                condition_met = left_val > right_val
            elif comparison == ">=":
                condition_met = left_val >= right_val

            if condition_met:
                pc = labels[jump_label]
                continue
        elif command == "END":
            break

        # Move to the next line
        pc += 1

    return output

if __name__ == "__main__":
    program1 = ["MOV A 1", "MOV B 2", "PRINT A", "PRINT B", "ADD A B", "PRINT A", "END"]
    program2 = ["MOV A 1", "MOV B 10", "begin:", "IF A >= B JUMP quit", "PRINT A", "PRINT B", "ADD A 1", "SUB B 1", "JUMP begin", "quit:", "END"]
    program3 = ["MOV A 1", "MOV B 1", "begin:", "PRINT A", "ADD B 1", "MUL A B", "IF B <= 10 JUMP begin", "END"]
    program4 = ["MOV N 50", "PRINT 2", "MOV A 3", "begin:", "MOV B 2", "MOV Z 0", "test:", "MOV C B", "new:", "IF C == A JUMP error", "IF C > A JUMP over", "ADD C B", "JUMP new", "error:", "MOV Z 1", "JUMP over2", "over:", "ADD B 1", "IF B < A JUMP test", "over2:", "IF Z == 1 JUMP over3", "PRINT A", "over3:", "ADD A 1", "IF A <= N JUMP begin", "END"]

    print(run(program1))
    print(run(program2))
    print(run(program3))
    print(run(program4))
