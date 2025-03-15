def basic_calculator():
    print("Welcome to the Python Calculator!")
    
    
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, %): ")
    num2 = float(input("Enter the second number: "))

    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero is not allowed."
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error! Modulus by zero is not allowed."
    else:
        return "Invalid operator! Please use one of (+, -, *, /, %)."

    return f"Result: {num1} {operator} {num2} = {result}"



if __name__ == "__main__":
    print(basic_calculator())
