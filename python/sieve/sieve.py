def primes(limit):
    non_primes = set([1])
    for n in range(2, limit + 1):
        for m in range(2 * n, limit + 1, n):
            non_primes.add(m)
    return sorted(list(set(range(1, limit + 1)) - non_primes))
