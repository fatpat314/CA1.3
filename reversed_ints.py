"""Write a function that will reverse a integer number
using a stack and return the reversed number as an integer.
For example, if your input number is 3479 the function will return 9743."""

def reverse_string_with_stack(input_int):
    my_stack = []
    reverse_ints = ""
    input_str = str(input_int)
    # step 1: put characters on the stack
    for character in input_str:
        # put characters into stack
        my_stack.append(character)
    # while the stack is not empty
    while len(my_stack) != 0:
        # setting character to be the top item in the stack
        # and removing that item from the stack
        character = my_stack.pop(-1)
        # concatinate charaters into a new string
        reverse_ints += character
    return int(reverse_ints)

print(reverse_string_with_stack(3479))
