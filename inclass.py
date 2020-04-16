# write a function to reverse a string without using string slices.

# I am going to want to put my string into a list.
# try to reverse the indexes.

def reverse(str):
    reversed_str = ""
    index = len(str) - 1
    while index >= 0:
        reversed_str += str[index]
        index -= 1
    print(reversed_str)
    return reversed_str

    # str = list(str)
    # count = len(str) - 1
    # new_list = []
    # # print(str)
    # # print(count)
    # for i in str:
    #     new_list.append(str[count])
    #     count = count - 1
    #     # print(i)
    # print(new_list)
    # for i in new_list:
    #     print(new_list[i])



reverse('What')
