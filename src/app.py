import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a*b

def div(dividend,divisor):
    if divisor == 0:
        return None
    return dividend / divisor

def log(a, b=10):
    return math.log(a, b)

def square(a):
    return a**2

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def sqrt(a):
    if a < 0: 
        return None
    return a ** .5

def pct(a):
    return a * 100
