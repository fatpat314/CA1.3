#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # This reverses the digits
    digits = digits[::-1]
    # Put the digits into a list
    digit_list = list(digits)
    # make a new list
    new_list = []
    # loop through each index of digit_list
    for i in digit_list:
        # if the content of that index is found in the alphabit
        if i in list(string.ascii_uppercase):
            # start a counter at 10
            count = 10
            # loop through each letter in the alphabit
            for letter in string.ascii_uppercase:
                # if the letter is equal to the content of the index
                if i == letter:
                    # add the quality of count to new_list
                    new_list.append(count)
                else:
                    # increase count by one
                    count += 1
        #else, if the content of that index if found in the alphabit
        elif i in list(string.ascii_lowercase):
            # start a counter at 10
            count = 10
            # loop through each letter in the alphabit
            for letter in string.ascii_lowercase:
                # if the latter is equal to the content of the index
                if i == letter:
                    # add the quality of count to new_list
                    new_list.append(count)
                else:
                    # increase count by one
                    count += 1
        # else, put the index into new_list
        else:
            new_list.append(i)

    d_num = 0
    # loop through the length of new_list
    for i in range(len(new_list)):
        # set number to be the index
        number = new_list[i]
        # convert that to an int
        number = int(number)
        print("number", number)
        # d_num increased by number times the base to the power of the index
        d_num += number * base**i
    return d_num

"""uncomment this to test if decode works"""
# print(decode("1010", 2))



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # TODO: Encode number in hexadecimal (base 16)
    """ input will be 26. output will be 1A """
    # make an empty string
    ret_str = ""
    # loop while the number is greater then 0
    while number > 0:
        # remainder from modulous
        remainder = number % base
        # number - remainder
        number -= remainder
        # divide number by base
        number = number // base
        # if remainder is greater than 9
        if remainder > 9:
            # remainder equals the content of the index in the alphabit
            remainder = string.ascii_lowercase[remainder-10]
        # conver to string
        ret_str = str(remainder) + ret_str
    return ret_str

"""uncomment this to see if encode works"""
# print(encode(42, 16))

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...

    old_number = decode(digits,base1)
    new_number = encode(int(old_number), base2)
    return new_number


"""uncomment this to see if convert works"""
# print(convert('A1', 16, 2))

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
