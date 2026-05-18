def add(n,m):
    a = n + m
    print(a)

def sub(n,m):
    s = n - m
    print(s)

def mult(n,m):
    mu = n * m

def div(n,m):
    d = n / m

n = int(input("Enter your first number: "))
m = int(input("Enter your second number: "))

print("What operation do you want to perform ?: [Add(add), Subtract(sub), Multiply(mult), Divide(div)]")

o = input()

o(n,m)
