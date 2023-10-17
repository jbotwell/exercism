price_set_of = [0, 800, 1520, 2160, 2560, 3000]


def total(basket):
    counts = [0, 0, 0, 0, 0, 0]
    for book in basket:
        counts[book] += 1
    counts = counts[1:]

    sets = []
    while not all(count == 0 for count in counts):
        counts.sort(reverse=True)
        in_set = 0
        for i, count in enumerate(counts):
            if count == 0:
                break
            else:
                counts[i] -= 1
                in_set += 1
        sets.append(in_set)

    while 3 in sets and 5 in sets:
        sets.remove(3)
        sets.remove(5)
        sets.append(4)
        sets.append(4)

    price = 0
    for a_set in sets:
        price += price_set_of[a_set]

    return price
