num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter what you want (Add=+, Sub=-, Multiply=*, Divide=/): ")

if operator == '+':
    print(f"Result: {num1 + num2}")
elif operator == '-':
    print(f"Result: {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator!")
