# from random import randint


# code_len = 7
# for i in range(200):
#     code = ''.join([str(randint(0, 9)) for i in range(code_len)])
#     print(code)

import string
import random


def activiation_creator(digit):
    code = ''
    for word in range(digit):
        code += random.choice(string.ascii_uppercase + string.digits)
    return code


def two_hundred_codes():
    data = []
    for count in range(200):
        digit = 12
        data.append(activiation_creator(digit))
    return data


if __name__ == '__main__':
    print(two_hundred_codes())
