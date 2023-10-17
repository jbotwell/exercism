actions = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str):
    todo = []
    for i, act in enumerate(binary_str[::-1]):
        if i == 4 and act == "1":
            todo = todo[::-1]
        elif act == "1":
            todo.append(actions[i])
    return todo
