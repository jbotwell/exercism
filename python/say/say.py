def say(number):
    if not 0 <= number < 1_000_000_000_000:
        raise ValueError("input out of range")
    thousands = ["", "thousand", "million", "billion"]
    ascending_digits = list(digits(number))
    groups = [ascending_digits[i : i + 3] for i in range(0, len(ascending_digits), 3)]

    if number == 0:
        return "zero"
    result = ""
    for i, group in enumerate(groups):
        if group == [0, 0, 0]:
            continue
        result = three_digit(*group) + " " + thousands[i] + " " + result

    return result.strip()


def digits(number):
    while number > 0:
        yield number % 10
        number = number // 10


def three_digit(*args):
    ones = args[0]

    if len(args) > 1:
        tens = args[1]
    else:
        tens = 0

    if len(args) > 2:
        hundreds = args[2]
    else:
        hundreds = 0
    return (hundred(hundreds) + " " + double_digit(ones, tens)).strip()


def double_digit(ones, tens):
    if tens == 1:
        return [
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ][ones]
    elif tens == 0:
        return one(ones)
    elif ones == 0:
        return ten(tens)
    else:
        return ten(tens) + "-" + one(ones)


def one(digit):
    return ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][
        digit
    ]


def ten(digit):
    return [
        "",
        "pass",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ][digit]


def hundred(digit):
    if digit == 0:
        return ""
    else:
        return one(digit) + " hundred"
    if hundreds == 0:
        return


print(say(100))
