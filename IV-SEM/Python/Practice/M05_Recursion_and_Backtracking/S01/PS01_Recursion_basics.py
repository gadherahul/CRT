#sum of n natural numbers
import code
from math import factorial


def sum_of_N(n):
    s = 0
    for i in range(1,n+1):
        s += i  
    return s
print(sum_of_N(5))#15
print(sum_of_N(10))#55

def sum_of_N(n):
    if n == 1:
        return 1
    return n + sum_of_N(n-1)

print(sum_of_N(5))#15
print(sum_of_N(10))#55  

def Factorial(n):
    if n == 0:
        return "no factorial -ves"
    elif n == 1:
        return 1
    return n * Factorial(n-1)
print(Factorial(5))#120
print(Factorial(0))#no factorial -ves

