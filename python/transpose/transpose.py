def transpose(lines):
    lines = lines.split("\n")
    longest_line = max(lines, key=len)
    result = [["\t" for _ in range(len(lines))] for _ in longest_line]
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            result[j][i] = char
    lines = list(map(lambda line: "".join(line), result))
    return "\n".join(strip_and_replace_tabs(lines))


def strip_and_replace_tabs(lines):
    return map(lambda l: l.rstrip("\t").replace("\t", " "), lines)
