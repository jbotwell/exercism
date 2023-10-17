class StackUnderflowError(Exception):
    pass


def evaluate(input_data: list[str]) -> list[int]:
    definitions = process_definitions(filter(is_definition, input_data))

    final_program = apply_definitions(definitions, input_data[-1])

    return eval_final_program(final_program)


def eval_final_program(processed: str) -> list[int]:
    stack = processed.split(" ")
    results = []

    for s in stack:
        try:
            if is_int(s):
                results.append(int(s))
            elif s in "+-*":
                second = results.pop()
                first = results.pop()
                results.append(eval("{} {} {}".format(first, s, second)))
            elif s == "/":
                second = results.pop()
                first = results.pop()
                if second == 0:
                    raise ZeroDivisionError("divide by zero")
                results.append(first // second)
            elif s == "dup":
                to_add = results.pop()
                results.append(to_add)
                results.append(to_add)
            elif s == "drop":
                results.pop()
            elif s == "over":
                results.append(results[-2])
            elif s == "swap":
                results[-1], results[-2] = results[-2], results[-1]
            else:
                raise ValueError("undefined operation")

        except IndexError:
            raise StackUnderflowError("Insufficient number of items in stack")

    return results


def process_definitions(definitions):
    mappings = {}
    for directive in definitions:
        directive = directive[1:-1].lower().strip().split(" ")

        word = directive[0]
        if is_int(word):
            raise ValueError("illegal operation")
        meaning = " ".join(directive[1:])

        if meaning in mappings:
            mappings[word] = mappings[meaning]
        else:
            mappings[word] = apply_definitions(mappings, meaning)

    return mappings


def apply_definitions(definitions, preprocessed):
    preprocessed = preprocessed.lower().split(" ")
    processed = []
    for p in preprocessed:
        if p in definitions:
            processed.append(definitions[p])
        else:
            processed.append(p)

    return " ".join(processed)


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def peek(stack):
    try:
        return stack[-1]
    except IndexError:
        return None


def is_definition(command):
    return len(command) >= 2 and command[0] == ":" and command[-1] == ";"
