def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    solutions = [0 for _ in range(target + 1)]
    solutions[0] = []

    for i in range(target + 1):
        relevant_coins = [c for c in coins if c <= i]
        for c in relevant_coins:
            if i - c == 0:
                solutions[i] = [c]
                continue
            if solutions[i - c] == 0:
                continue
            if solutions[i] == 0 or len(solutions[i - c]) + 1 < len(solutions[i]):
                solutions[i] = solutions[i - c] + [c]

    if solutions[target] == 0:
        raise ValueError("can't make target with given coins")
    return sorted(solutions[target])
