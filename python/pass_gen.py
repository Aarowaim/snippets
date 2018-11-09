import string
import random

r = random.SystemRandom()


def new_pass(size):
    return [r.choice(list(set(string.printable) - set(string.whitespace)))
            for _ in range(size)]


if __name__ == '__main__':
    size = None
    while not size:
        try:
            size = int(
                input("Please enter a number of digits for a password:\n"))
        except ValueError as e:
            print(e)

    print(''.join(new_pass(size)))
