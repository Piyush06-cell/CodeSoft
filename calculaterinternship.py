
a = int(input("Enter your 1st number: "))

operator = input("Please input operator (+, -, *, /): ")


b = int(input("Enter your 2nd number: "))


if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"


print(f"The result is: {result}")
