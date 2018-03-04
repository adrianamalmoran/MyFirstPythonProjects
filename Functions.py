def stringFunction():
    print("Hello!")

var = 5

def returnVar(var):
    print(var)

stringFunction()
returnVar(var)


a = 5
b = 10
c = 50

def minus(a,b):
    return a-b

def product(a,b,c):
    x = a * b * c
    return x

minus(a,b)
product(a,b,c)

d = 3.1
e = 4.5
f = 8.3

def quotient(d,e):
    x = d/e
    return x

def second_quotient(a,b,c):
    x = quotient(a,b)
    y = x/c
    return y

print("%.2f"%quotient(d,e))
print("%.2f"%second_quotient(d,e,f))
