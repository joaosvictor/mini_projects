from math import *

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    for y in range(3, ceil(sqrt(x)) + 1, 2):
        if x % y == 0:
            return False

    return True

def generate_primes(num_to_generate):
    primes = [2]
    number = 3

    while len(primes) <= num_to_generate:
        if is_prime(number):
            primes.append(number)
        number += 2

    return primes

print(generate_primes(10000).pop())
