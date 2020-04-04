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
    digits = digits[::-1]

    digit_list = list(digits)
    new_list = []
    for i in digit_list:
        if i in list(string.ascii_uppercase):
            count = 10
            for letter in string.ascii_uppercase:
                if i == letter:
                    new_list.append(count)
                else:
                    count += 1
        elif i in list(string.ascii_lowercase):
            count = 10
            for letter in string.ascii_lowercase:
                if i == letter:
                    new_list.append(count)
                else:
                    count += 1
        else:
            new_list.append(i)

    d_num = 0
    for i in range(len(new_list)):
        number = new_list[i]
        number = int(number)
        print("number", number)
        d_num += number * base**i
    return d_num


# print(decode("23G", 36))



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    """ input will be 5. ouput 0101 """


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
    # TODO: Encode number in any base (2 up to 36)
    # ...


print(encode(42, 16))


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
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


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
