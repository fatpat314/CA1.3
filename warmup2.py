# input two arrays
# find the elements that two arrays have in common

# def intersection(list1, list2):
#     item_dictionary = {}
#     intersection = []
#     for item in list1:
#         if item not in item_dictionary.keys():
#             item_dictionary[item] = 1
#         else:
#             item_dictionary[item] += 1
#     for item in list2:
#         if item in item_dictionary.keys():
#             item_dictionary[item] += 1
#
#     for key,value in item_dictionary.items():
#         if value > 1:
#             intersection.append(key)
#     return intersection
#
# print(intersection([1,5,7,9], [2,3,1,9]))#expect [1,9]

def get_tree_sum(node, sum):
    if node is not None:
        get_tree_sum(node.left)
        # visit
        sum += node.data
        get_tree_sum(node.right)

def get_sum_BST(node):
    if node == None:
        return 0
    return node.data + get_sum_BST(node.left) + get_sum_BST(node.right)
