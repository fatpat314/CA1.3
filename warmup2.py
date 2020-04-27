# input two arrays
# find the elements that two arrays have in common

def intersection(list1, list2):
    item_dictionary = {}
    intersection = []
    for item in list1:
        if item not in item_dictionary.keys():
            item_dictionary[item] = 1
        else:
            item_dictionary[item] += 1
    for item in list2:
        if item in item_dictionary.keys():
            item_dictionary[item] += 1

    for key,value in item_dictionary.items():
        if value > 1:
            intersection.append(key)
    return intersection

print(intersection([1,5,7,9], [2,3,1,9]))#expect [1,9]
