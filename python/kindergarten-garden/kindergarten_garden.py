default_students = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]

symbol_plants = {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets"}


class Garden:
    def __init__(self, diagram, students=default_students):
        self.students = sorted(students)
        self.plots = split_into_subplots(diagram.split("\n"))

    def plants(self, name):
        i = self.students.index(name)
        return self.plots[i]


def split_into_subplots(plots):
    subplots = []
    for i in range(0, len(plots[0]), 2):
        new_sub = []
        new_sub.append(symbol_plants[plots[0][i]])
        new_sub.append(symbol_plants[plots[0][i + 1]])
        new_sub.append(symbol_plants[plots[1][i]])
        new_sub.append(symbol_plants[plots[1][i + 1]])

        subplots.append(new_sub)

    return subplots
