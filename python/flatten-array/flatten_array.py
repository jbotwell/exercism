def flatten(iterable):
    results = []
    for member in filter(lambda m: m != None, iterable):
        if not isinstance(member, list):
            results.append(member)
        else:
            results += flatten(member)

    return results
