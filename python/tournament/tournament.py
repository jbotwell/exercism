def tally(rows):
    results = extract_results(rows)
    table = [("Team                           | MP |  W |  D |  L |  P", float("inf"))]

    for k, v in results.items():
        table.append(make_row(k, v))

    table.sort()
    table.sort(key=lambda row: row[1], reverse=True)
    return list(map(lambda row: row[0], table))


def make_row(team, results):
    pieces = []
    pieces.append(team.ljust(30, " "))
    for r in results:
        pieces.append(str(r).rjust(2, " "))
    return (" | ".join(pieces), results[-1])


def extract_results(rows):
    results = {}
    for r in rows:
        one_result(r, results)
    return results


def one_result(result_string, results):
    team_1, team_2, result = result_string.split(";")

    try:
        results[team_1][0] += 1
    except KeyError:
        results[team_1] = [1, 0, 0, 0, 0]

    try:
        results[team_2][0] += 1
    except KeyError:
        results[team_2] = [1, 0, 0, 0, 0]

    if result == "win":
        results[team_1][1] += 1
        results[team_2][3] += 1
        results[team_1][4] += 3
    elif result == "loss":
        results[team_2][1] += 1
        results[team_1][3] += 1
        results[team_2][4] += 3
    elif result == "draw":
        results[team_1][2] += 1
        results[team_2][2] += 1
        results[team_1][4] += 1
        results[team_2][4] += 1
