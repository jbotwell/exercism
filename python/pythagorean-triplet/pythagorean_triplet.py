from math import sqrt, ceil, gcd


def triplets_with_sum(number):
    return [triple for triple in euclids_generator(number) if sum(triple) == number]


def euclids_generator(limit):
    for n in range(1, ceil(sqrt(limit))):
        for m in range(n + 1, ceil(sqrt(limit))):
            if gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0):
                a, b, c = m**2 - n**2, 2 * n * m, m**2 + n**2
                k = 1
                while k * (a + b + c) <= limit:
                    yield sorted([a * k, b * k, c * k])
                    k += 1
