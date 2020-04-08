# [0,1,1,2,3,5,8,13, ...]
# n = 0
# list = []
# def fib(n):
#     list(n)
# fib(n)

# f(n) = f(n-1) + f(n-2)
# 0, 1

def fib(n):
    # base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))
