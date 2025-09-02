def add(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def mul(a, b):
    c = a * b
    return c
    
    

def div(a, b):
    c = a // b
    return c


def power(base, pow):
    c = base**pow
    return c


def square(base):
    c = base * base
    return c


def greet(이름="낯선자", 나이=20):
    if 이름 == "낯선자" and 나이 == 20:
        return "안녕하신가 낯선자!"
    elif 이름 == "마법사": 
        return "안녕하십니까 마법사!"
    elif 나이 == 4:
        return "안녕 낯선자!"
    
     
    
