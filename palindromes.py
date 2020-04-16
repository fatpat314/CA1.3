#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # take the input and turn it into a list.
    text = list(text)
    # make veriables for front and back
    left = 0
    right = len(text) -1
    # while  front is less than back.
    while left < right:
        # if front does not = back
        if text[left] != text[right]:
            # return none
            print("None")
            return False
        else:
            left += 1
            right -= 1

        print("works")
    return True
# print(is_palindrome_iterative("deed"))
# print(is_palindrome_iterative("not"))

    # pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # if left and right == :
    text = text.lower()
    text = text.strip()
    print(text)
    text_list = list(text)
    left = 0
    right = len(text_list) -1

    if text == '' or len(text_list) == 1:
        # print("wrong")
        return True

    if text_list[left] != text_list[right]:
        # print("wrong")
        return False



    # if left == right:
    #     print("yes")
    if left == right:
        print("yes")

        is_palindrome_recursive(text, left + 1, right - 1)
        # print("yes")
        # count += 1
    return True
    # return True

# print(is_palindrome_recursive("deed"))
print(is_palindrome_recursive("A B"))
# print(is_palindrome_recursive(""))

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
