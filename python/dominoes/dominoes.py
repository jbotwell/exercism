Dominoes = list[tuple[int, int]]


def can_chain(dominoes: Dominoes) -> None | Dominoes:
    # use first as first; any domino will work
    if dominoes == []:
        return []
    else:
        valid, chain = can_chain_tramp([dominoes[0]], dominoes[1:])
        if valid:
            return chain
    return None


def can_chain_tramp(chain: Dominoes, dominoes: Dominoes) -> tuple[bool, Dominoes]:
    if dominoes == []:
        return (is_valid(chain), chain)

    for i, d in enumerate(dominoes):
        end = chain[-1][1]
        if d[0] == end or d[1] == end:
            if d[1] == end:
                d = d[::-1]
            valid, test_chain = can_chain_tramp(
                chain + [d], dominoes[:i] + dominoes[i + 1 :]
            )
            if valid:
                return (True, test_chain)

    return (False, [])


def is_valid(chain: Dominoes) -> bool:
    return chain[0][0] == chain[-1][1]
