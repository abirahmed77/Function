def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

op = input("Enter an Operator [ + , - , * , / ] : ")

if op == "+":
    res = add(num1, num2)
    print(f"{num1} + {num2} = {res}")
    
elif op == "-":
    res = sub(num1, num2)
    print(f"{num1} - {num2} = {res}")
    
elif op == "x":
    res = mult(num1, num2)
    print(f"{num1} * {num2} = {res}")
    
elif op == "/":
    res = div(num1, num2)
    print(f"{num1} / {num2} = {res}")