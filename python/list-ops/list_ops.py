def append(list1, list2):
    return list1 + list2


def concat(lists):
    results = []
    for l in lists:
        results += l
    return results


def filter(function, list):
    results = []
    for l in list:
        if function(l):
            results.append(l)
    return results


def length(list):
    result = 0
    for e in list:
        result += 1
    return result


def map(function, list):
    result = []
    for e in list:
        result.append(function(e))
    return result


def foldl(function, list, initial):
    result = initial
    for e in list:
        result = function(result, e)
    return result


def foldr(function, list, initial):
    result = initial
    for e in list[::-1]:
        result = function(result, e)
    return result


def reverse(list):
    result = []
    for e in list:
        result = [e] + result
    return result
