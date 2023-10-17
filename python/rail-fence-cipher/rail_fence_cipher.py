def encode(message, rails):
    results = ["" for _ in range(rails)]
    row_change = -1
    rail = 0

    for char in message:
        results[rail] += char
        if rail == 0 or rail == rails - 1:
            row_change *= -1
        rail += row_change

    return "".join(results)


def decode(encoded_message, rails):
    n_in_rails = count_chars_in_rails(len(encoded_message), rails)
    cut_up_message = []
    end = 0
    print(n_in_rails)
    for count in n_in_rails:
        start, end = end, end + count
        cut_up_message.append(list(encoded_message[start:end]))

    row_change = -1
    rail = 0
    results = ""
    for _ in encoded_message:
        print(cut_up_message)
        char = cut_up_message[rail].pop(0)
        results += char
        if rail == 0 or rail == rails - 1:
            row_change *= -1
        rail += row_change

    return results


def count_chars_in_rails(num_chars, rails):
    row_change = -1
    rail = 0
    results = [0 for _ in range(rails)]
    for i in range(num_chars):
        results[rail] += 1
        if rail == 0 or rail == rails - 1:
            row_change *= -1
        rail += row_change
    return results
