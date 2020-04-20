#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

def punctuation(text):
    "There must be a better way"
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace("-", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("\'", "")
    return text

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # take the input and turn it into a list.
    # remove all punctuation and spaces
    text = punctuation(text)
    print(text)
    # put the letters of text into a list
    text_list = list(text)
    text = list(text)
    # make veriables for front and back
    # let left to 0 and right to the length of text -1
    left = 0
    right = len(text) -1
    # while  left is less than right.
    while left < right:
        # if front does not == back
        if text[left] != text[right]:
            print("None")
            # return False
            return False
        else:
            # increse left by 1
            left += 1
            # decrese right by 1
            right -= 1

        print("works")
    # return true
    return True
# print(is_palindrome_iterative("deed"))
# print(is_palindrome_iterative("not"))

    # pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here

    "There must be a better way to remove punctuation"
    # remove all punctuation and spaces from text
    text = punctuation(text)
    print(text)
    # put the letters of text into a list
    text_list = list(text)

    # If this is the first pass
    if left is None and right is None:
        # set left to 0
        left = 0
        # set right to the length of text_list - 1
        right = len(text_list) - 1
        # set truth to none
        truth = None
    # If text only has one letter or is empth
    if len(text_list) == 1 or text == '': #√
        # palindrome is true
        truth = True
    # if we are at the end
    if left >= right:
        # palindrome is true
        truth = True
        return truth
    # if the letters in the complemetery index does not match
    if text_list[left] != text_list[right]:
        print(left,right)
        # palindrom is False
        truth = False
        print("Truth = ", truth)
        print(text_list[left], text_list[right])
        return truth
    # if there are still more letters to check
    if left < right:
        # if the letters in the complementery indes do match
        if text_list[left] == text_list[right]:
            print(left,right)
            # palindrom is true
            truth = True
            print("Truth = ", truth)
            print(text_list[left], text_list[right])
            # bring left and right in by one letter and check again
            return is_palindrome_recursive(text, left + 1, right - 1)

# print(is_palindrome_recursive("deed"))
print(is_palindrome_recursive("taco? cat."))
# print(is_palindrome_recursive("ABCZBA"))
# print(is_palindrome_recursive("AZ"))
# print(is_palindrome_recursive("BB"))
# print(is_palindrome_recursive("Bb"))
# print(is_palindrome_recursive("A"))
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
