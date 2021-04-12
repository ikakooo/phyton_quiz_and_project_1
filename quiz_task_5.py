import random

def factorialWithFor(a):
    factorial=1
    for i in range(1,a+1):
        factorial*=i
    return factorial
    
def factorialWithWhile(a):
    factorial =1
    while a>1:
        factorial*=a
        a-=1
    return factorial
    
def factorialWithRecursion(a):
    if a ==1:
        return a
    else:
        return a*factorialWithRecursion(a-1)
    
def factorial(x):
    a=random.randint(0,2)
    print(a)


    if a==0:
        return factorialWithFor(x)
    if a==1:
        return factorialWithWhile(x)
    else:
        return factorialWithRecursion(x)



        
        
print(factorial(10))