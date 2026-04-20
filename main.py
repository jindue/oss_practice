def add(A, B):
    return A + B
def sub(A, B):
    return A - B
def mul(A, B):
    return A * B
def div(A, B):
    return A / B

A = int(input("A:"))
B = int(input("B:"))

op = input("op: + - * /")

if op == "+":
    print(A + B)
elif op == "-":
    print(A - B)
elif op == "*":
    print(A * B)
    print(A / B)
    pass
elif op == "/":
    pass