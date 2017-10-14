#!/usr/bin/env python
import string
from itertools import chain
from random import choice, sample


def mkpasswd(length=12, digits=4, upper=3, lower=3):
    lowercase = string.lowercase
    uppercase = string.uppercase
    salt = '!@#$%^&*()><?'
    password = list(
    chain(
    (choice(uppercase) for _ in range(upper)),
    (choice(lowercase) for _ in range(lower)),
    (choice(string.digits) for _ in range(digits)),
    (choice(salt) for _ in range((length - digits - upper - lower)))
    )
    )
    return "".join(sample(password, len(password)))
if __name__ == '__main__':
    print mkpasswd()
