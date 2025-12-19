a = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

if op == "/" and b == 0:
    print("Division by zero is not allowed")
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
