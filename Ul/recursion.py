def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci (i):
    if i == 0:
        return 0
    elif  i == 1:
        return 1
    else:   
        return fibonacci(i - 1) + fibonacci(i - 2)

def length(l):
    if not l :
        return 0
    else:
        return length(l[1:]) + 1

print(factorial(10))
print(fibonacci(10))
print(length([1, 2, 3]))
