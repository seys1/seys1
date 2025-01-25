from random import randint, choice

def email():

    min_length = 15
    max_length = 20

    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    gen_abc = ''.join(choice(abc) for _ in range(randint(min_length, max_length)))

    email = gen_abc + '@gmail.com'

    return email