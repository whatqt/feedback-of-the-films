import random


def random_id_ticket():
    numbers_str = '123456789'
    letters_str = 'qwertyuiopasdfghjklzxcvbnm'
    lettersUP_str = letters_str.upper()
    symbols = numbers_str+letters_str+lettersUP_str
    return ''.join([random.choice(symbols) for i in range(11)])

