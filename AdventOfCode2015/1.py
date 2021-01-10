
with open('resources/1.txt', 'r') as text:
    instructions = text.read()


def part_one():
    up = instructions.count("(")
    down = instructions.count(")")

    position = 0 + up - down

    print(position)


def part_two():
    position = 0
    for index, item in enumerate(instructions):
        if item == "(":
            position += 1
        elif item == ")":
            position -= 1
        if position == -1:
            print(index+1)
            exit(0)


part_one()
part_two()
