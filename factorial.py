# def factorial(n):



def factorial_iterative(n):
    factorial = 1
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def factorial_recursive(n):
    # 3! == 3*2*1
    # 3! == 3*2!
    if n == 1:
        return 1
    else:
        result = factorial_recursive(n-1)
        return result * n
