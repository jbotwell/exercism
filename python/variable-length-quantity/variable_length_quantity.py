def encode(numbers):
    results = []
    for n in numbers:
        results += encode_one(n)
    return results


def decode(bytes_):
    if bytes_[-1] & 0x80 > 0:
        raise ValueError("incomplete sequence")
    results = []
    number_bytes = []
    for next_byte in bytes_:
        number_bytes.append(next_byte)
        if not (next_byte & 0x80 > 0):
            results.append(decode_one(number_bytes))
            number_bytes = []
    return results


def decode_one(bytes_):
    result = 0
    for i, b in enumerate(bytes_[::-1]):
        b &= 0x7F
        result |= b << (7 * i)
    return result


def encode_one(n):
    results = []
    last = True
    while n > 0:
        n, mod = n >> 7, n & 0x7F
        if last:
            results.insert(0, mod)
            last = False
        else:
            results.insert(0, mod | 0x80)

    if len(results) > 0:
        return results
    else:
        return [0x00]
