def recite(start, take=1):
    results = []
    for n in range(start, start - take, -1):
        results += make_verse(n)

    # remove last ""
    results.pop()

    return results


def make_verse(bottles):
    words = [
        "no",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]
    if bottles == 1:
        first_sing_plur = "bottle"
        second_sing_plur = "bottles"
    elif bottles == 2:
        first_sing_plur = "bottles"
        second_sing_plur = "bottle"
    else:
        first_sing_plur = "bottles"
        second_sing_plur = "bottles"

    return [
        f"{words[bottles].capitalize()} green {first_sing_plur} hanging on the wall,",
        f"{words[bottles].capitalize()} green {first_sing_plur} hanging on the wall,",
        f"And if one green bottle should accidentally fall,",
        f"There'll be {words[bottles - 1]} green {second_sing_plur} hanging on the wall.",
        "",
    ]
