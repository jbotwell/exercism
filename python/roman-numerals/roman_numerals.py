digits = (("I", "V"), ("X", "L"), ("C", "D"), ("M", "non-existent"), ("non-existent"))


def roman(number):
    result = ""
    place = 0
    for n in get_digits(number):
        result = one_digit(n, place) + result
        place += 1
    return result


def get_digits(number):
    while number > 0:
        yield number % 10
        number = number // 10


def one_digit(n, place):
    one = digits[place][0]
    five = digits[place][1]
    ten = digits[place + 1][0]

    if n == 0:
        return ""
    elif n == 1:
        return one
    elif n == 2:
        return one * 2
    elif n == 3:
        return one * 3
    elif n == 4:
        return one + five
    elif n == 5:
        return five
    elif n == 6:
        return five + one
    elif n == 7:
        return five + one * 2
    elif n == 8:
        return five + one * 3
    elif n == 9:
        return one + ten
    else:
        return ""
