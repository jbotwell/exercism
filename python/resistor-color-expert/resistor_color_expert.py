color_numbers = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9",
}

color_tolerances = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def resistor_label(colors):
    if len(colors) == 1:
        return color_numbers[colors[0]] + " ohms"

    tolerance = "±" + color_tolerances[colors[-1]]
    multiplier = int(color_numbers[colors[-2]])

    digits = ""
    for color in colors[:-2]:
        digits = digits + color_numbers[color]

    ohms = int(digits) * 10**multiplier

    return format_ohms(ohms) + tolerance


def format_ohms(ohms):
    prefix = ["", "kilo", "mega", "giga"]
    prefix_index = 0
    while ohms >= 1000:
        ohms /= 1000
        prefix_index += 1
    if ohms % 1 == 0:
        ohms = int(ohms)
    return f"{ohms} {prefix[prefix_index]}ohms "
