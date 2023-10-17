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
    print("colors 0", colors[0], color_numbers[colors[0]])
    return color_numbers[colors[0]] * 10 + color_numbers[colors[1]]
