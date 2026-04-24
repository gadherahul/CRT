def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))#5
print(fibonacci(10))#55

def GCD (a,b):
    if b == 0:
        return a
    return GCD(b,a%b)   
print(GCD(4,10))#2

#Recursive approach
def GCD (a,b):
    if a == b:
        return a
    elif a > b:
        return GCD(a-b,b)
    else:
        return GCD(a,b-a)
print(GCD(4,10))#2









                