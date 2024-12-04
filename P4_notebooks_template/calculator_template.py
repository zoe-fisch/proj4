def add(x, y):
    # start student code here
    return x + y
    # end student code here

def subtract(x, y):
    # start student code here
    return x - y
    # end student code here

def multiply(x, y):
    # start student code here
    return x * y
    # end student code here

def divide(x, y):
    # start student code here. Note be aware of divide by zero
    if y == 0:
        print("Divide by zero error!!!")
        return None
    else:
        return x / y
    # end student code here

def get_number(prompt):
    # start student code here. Use "input". 
    num = float(input(prompt))
    return num
    # end student code here


def get_operator():
    # start student code here. Use "input" and "in". 
    op = input("Please type a math operator (one of: + - * / or q to quit): ")
    return op
    # end student code here

def pocket_calculator():
    # Step 1: Get the initial number from the user
    # Step 2: Get an operator from the user
    # Step 3: Check if the operator is 'q' to quit
    # Step 4: Get another number from the user
    # Step 5: Calculate the result based on the operator and print the equation
    # Print the full equation. Use "print()".
    # Step 6: Save the result as the first number for the next operation. Loop through While until `q` to quit.

    ##### start student code here. 
    num1 = get_number("Enter a number: ")
    while True:
        op = get_operator()
        if op == "q":
            print("Calculator quitting now!")
            break
        num2 = get_number("Enter a number: ")
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation")
            continue  # Skip to the next iteration if the operation is invalid

        if result is None:  # Skip updating or printing if the result is invalid
            continue

        if num2 != 0:
            print(num1, " ", op, " ", num2, " = ", result)
        
        num1 = result

    ##### end student code herec



# Run the calculator by calling the function
pocket_calculator()
