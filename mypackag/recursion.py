def sum_array(array):
    total = 0
    for value in array:
        total += value
    return total


def fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

def reverse(word):
    return word[::-1]
