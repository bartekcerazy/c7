

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

print(add(5, 3))
print(subtract(10, 4))
print(multiply(6, 7))
print(divide(15, 3))
print(divide(10, 0))