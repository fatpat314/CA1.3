"""Imagine you are writing a function for a new
code editor that will check if a string expression
contains correctly balanced parentheses.
This function will return true if the string expression is
correct and false if not"""

def check_brackets(expression):
    # going to push open on stack
    # if find an end compate to top of stack
    open_brackets = ["{","[","("]
    closed_brackets = ["}","]",")"]
    bracket_stack = []

    for character in expression:
        if character in open_brackets:#add open bracket to stack
            bracket_stack.append(character)
        if character in closed_brackets:
            if len(bracket_stack) != 0:
                return False
            position = closed_brackets.index(character)

            open_bracket_at_top = bracket_stack.pop(len(bracket_stack) -1)

            # check if the open bracket at the
            if open_bracket_at_top != open_brackets[position]:
                return False
    if len(bracket_stack)==0:
        return True
    else:
        return False


print(check_brackets("(()())"))
print(check_brackets("[[hello]], ((jess)"))
print(check_brackets("[[hello]], ((jess))("))







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
