def iterative_search(list, target):
    for item in list:
        if item == target:
            return item
    return "not found"

def recursive_search(list, target):
    n = 0
    if n == target:
        return n
    else:
        n+=1
        recursive_search(list, target)
    return list[n]
