num1 = float(input('Please enter your first number: '))
num2 = float(input('Please enter your second number: '))

operation = input('Please enter the operation you would like to perform (+-*/): ')

if operation in ['+', '-', '*', '/']:
    print(f"{float(num1)} {operation} {float(num2)}")
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)
else:
    print('Invalid operation')
    


