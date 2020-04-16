
def compute_sum(n):
    factorial = 1
    result = 1
    for i in range(1, n+1):
        result = result + i

    result = result - 1
    print(result)
    return result
    





compute_sum(5)
