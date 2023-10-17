def proverb(*wants, qualifier=None):
    results = []

    for i1, w2 in enumerate(wants[1:]):
        results.append(make_sentence(wants[i1], w2))

    if len(wants) > 0:
        results.append(make_finisher(wants[0], qualifier))

    return results


def make_sentence(want1, want2):
    return "For want of a {} the {} was lost.".format(want1, want2)


def make_finisher(want, qualifier):
    if qualifier == None:
        return "And all for the want of a {}.".format(want)
    else:
        return "And all for the want of a {} {}.".format(qualifier, want)
