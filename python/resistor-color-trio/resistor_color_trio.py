color_numbers = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def value(colors):
    return color_numbers[colors[0]] * 10 + color_numbers[colors[1]]


def get_prefix_and_multiplier(exponent):
    prefix_index = 0
    while exponent >= 3:
        prefix_index += 1
        exponent -= 3
    prefix = ["", "kilo", "mega", "giga"][prefix_index]
    return (prefix, 10**exponent)


def label(colors):
    exponent = color_numbers[colors[2]]
    if colors[1] == "black":
        exponent += 1
        num = color_numbers[colors[0]]
    else:
        num = value(colors)
    prefix, multiplier = get_prefix_and_multiplier(exponent)
    return str(num * multiplier) + " " + prefix + "ohms"
