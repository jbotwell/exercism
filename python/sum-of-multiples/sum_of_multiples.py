def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    counted_points = set([])
    for item in [m for m in multiples if m != 0]:
        values = range(item, limit, item)
        counted_points |= set(values)
    return sum(counted_points)
