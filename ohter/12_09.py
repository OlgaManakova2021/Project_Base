import random

def print_char():
    d = 0
    while d < 40:
        #rand_char = chr(randomint (300, 400))
        print(chr(random.randint (1050, 1110)),end='')
        d += 1

print_char()