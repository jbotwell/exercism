def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not all(map(lambda d: 0 <= d < input_base, digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    return num_to_list(output_base, list_to_num(input_base, digits))


def list_to_num(base, digits):
    sum = 0

    for i, d in enumerate(digits[::-1]):
        sum += base**i * d

    return sum


def num_to_list(base, n):
    digits = []

    place = 0
    while n > 0:
        digits.append(n % base)
        n = n // base
        place += 1

    if digits == []:
        return [0]

    else:
        return digits[::-1]
