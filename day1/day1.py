
def change_direction(direction, step):
    if "R" in step:
        direction += 1
        if direction > 3:
            direction = 0
    elif "L" in step:
        direction -= 1
        if direction < 0:
            direction = 3
    else:
        raise Exception("Unknown step")
    return direction


def move(direction, step):
    num_step = int(step[1:])
    if direction == 0:
        return (0, num_step)
    elif direction == 1:
        return (num_step, 0)
    elif direction == 2:
        return(0, -num_step)
    else:
        return (-num_step, 0)


def baby_steps(direction, step):
    num_step = int(step[1:])
    if direction == 0:
        return [(0, 1) for x in range(0, num_step)]
    elif direction == 1:
        return [(1, 0) for x in range(0, num_step)]
    elif direction == 2:
        return [(0, -1) for x in range(0, num_step)]
    else:
        return [(-1, 0) for x in range(0, num_step)]

def find_distance(steps):
    total_x = 0
    total_y = 0
    direction = 3
    for step in steps:
        direction = change_direction(direction, step)
        x, y = move(direction, step)
        total_x += x
        total_y += y
    return (total_x, total_y)


def find_first_twice(steps):
    total_x = 0
    total_y = 0
    direction = 3
    map = []
    map.append((0, 0))

    for step in steps:
        direction = change_direction(direction, step)
        bs = baby_steps(direction, step)
        for x, y in bs:
            total_x += x
            total_y += y
            if (total_x, total_y) in map:
                return (total_x, total_y)
            else:
                map.append((total_x, total_y))
    raise Exception("No match")


if __name__ == "__main__":
    example = ("R5", "L5", "R5", "R3")
    x, y = find_distance(example)
    answer = abs(x) + abs(y)
    assert answer == 12

    example2 = ("R8", "R4", "R4", "R8")
    x, y = find_first_twice(example2)
    print(x, y)
    assert abs(x) + abs(y) == 4

    init_data = "R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5"
    data = init_data.split(", ")
    x, y = find_distance(data)
    answer = abs(x) + abs(y)
    print(answer)

    x, y = find_first_twice(data)
    answer = abs(x) + abs(y)
    print(answer)
