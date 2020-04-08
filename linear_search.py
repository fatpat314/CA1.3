def iterative_search(list, target):
    for item in list:
        if item == target:
            return item
    return "not found"

# def recursive_search(list, target):
#     n = 0
#     if n == target: #base case
#         return n
#     else:
#         n+=1
#         recursive_search(list, target)
#     return list[n]

def recursive_search(list, taret, index = 0):
    if list[index] == target: #base case
        return target
    if index == len(list):
        return None #not found
    else: #recursive case
        return recursive_search(list, target, index + 1)
