"""Imagine you are writing a function for a new
code editor that will check if a string expression
contains correctly balanced parentheses.
This function will return true if the string expression is
correct and false if not"""

# def check_brackets(expression):
#     # going to push open on stack
#     # if find an end compate to top of stack
#     open_brackets = ["{","[","("]
#     closed_brackets = ["}","]",")"]
#     bracket_stack = []
#
#     for character in expression:
#         if character in open_brackets:#add open bracket to stack
#             bracket_stack.append(character)
#         if character in closed_brackets:
#             if len(bracket_stack) != 0:
#                 return False
#             position = closed_brackets.index(character)
#
#             open_bracket_at_top = bracket_stack.pop(len(bracket_stack) -1)
#
#             # check if the open bracket at the
#             if open_bracket_at_top != open_brackets[position]:
#                 return False
#     if len(bracket_stack)==0:
#         return True
#     else:
#         return False
#
#
# print(check_brackets("(()())"))
# print(check_brackets("[[hello]], ((jess)"))
# print(check_brackets("[[hello]], ((jess))("))


# def reverse_str(str):
#     reversed = ""
#     stack = []
#     str_list = list(str)
#     for i in str_list:
#         stack.append(i)
#     # print(stack)
#     index = len(stack) - 1
#     for i in stack:
#         # print(stack[index])
#         reversed = ...
#         print(index)

        # print(reversed)
    # return reversed
def reverse_string_with_stack(input_string):
    my_stack = []
    reverse_str = ""
    # step 1: put characters on the stack
    for character in input_string:
        # put characters into stack
        my_stack.append(character)
    # while the stack is not empty
    while len(my_stack) != 0:
        # setting character to be the top item in the stack 
        # and removing that item from the stack
        character = my_stack.pop(-1)
        # concatinate charaters into a new string
        reverse_str += character
    return reverse_str

print(reverse_string_with_stack("abc"))




    # print(i)


# print(reverse_str("abracadabra"))




#     str = list(str)
#     count1 = 0
#     count2 = 0
#     for i in str:
#         if i == "[":
#             count1 += 1
#         if i == "]":
#             count2 += 1
#         if i == "{":
#             count1 += 1
#         if i == "}":
#             count2 +=1
#         if i == ""
#     print(count1, count2)
#     if count1 == count2:
#         print("true")
#     else:
#         print("false")
#
#
# parentheses("[{}{})(]")
