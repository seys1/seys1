from random import randint, choice

def username():

    min_length = 15
    max_length = 20

    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    HPV_Username = ''.join(choice(abc) for _ in range(randint(min_length, max_length)))

    return HPV_Username