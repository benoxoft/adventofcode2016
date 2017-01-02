input = """move position 0 to position 3
rotate right 0 steps
rotate right 1 step
move position 1 to position 5
swap letter h with letter b
reverse positions 1 through 3
swap letter a with letter g
swap letter b with letter h
rotate based on position of letter c
swap letter d with letter c
rotate based on position of letter c
swap position 6 with position 5
rotate right 7 steps
swap letter b with letter h
move position 4 to position 3
swap position 1 with position 0
swap position 7 with position 5
move position 7 to position 1
swap letter c with letter a
move position 7 to position 5
rotate right 4 steps
swap position 0 with position 5
move position 3 to position 1
swap letter c with letter h
rotate based on position of letter d
reverse positions 0 through 2
rotate based on position of letter g
move position 6 to position 7
move position 2 to position 5
swap position 1 with position 0
swap letter f with letter c
rotate right 1 step
reverse positions 2 through 4
rotate left 1 step
rotate based on position of letter h
rotate right 1 step
rotate right 5 steps
swap position 6 with position 3
move position 0 to position 5
swap letter g with letter f
reverse positions 2 through 7
reverse positions 4 through 6
swap position 4 with position 1
move position 2 to position 1
move position 3 to position 1
swap letter b with letter a
rotate based on position of letter b
reverse positions 3 through 5
move position 0 to position 2
rotate based on position of letter b
reverse positions 4 through 5
rotate based on position of letter g
reverse positions 0 through 5
swap letter h with letter c
reverse positions 2 through 5
swap position 7 with position 5
swap letter g with letter d
swap letter d with letter e
move position 1 to position 2
move position 3 to position 2
swap letter d with letter g
swap position 3 with position 7
swap letter b with letter f
rotate right 3 steps
move position 5 to position 3
move position 1 to position 2
rotate based on position of letter b
rotate based on position of letter c
reverse positions 2 through 3
move position 2 to position 3
rotate right 1 step
move position 7 to position 0
rotate right 3 steps
move position 6 to position 3
rotate based on position of letter e
swap letter c with letter b
swap letter f with letter d
swap position 2 with position 5
swap letter f with letter g
rotate based on position of letter a
reverse positions 3 through 4
rotate left 7 steps
rotate left 6 steps
swap letter g with letter b
reverse positions 3 through 6
rotate right 6 steps
rotate based on position of letter c
rotate based on position of letter b
rotate left 1 step
reverse positions 3 through 7
swap letter f with letter g
swap position 4 with position 1
rotate based on position of letter d
move position 0 to position 4
swap position 7 with position 6
rotate right 6 steps
rotate based on position of letter e
move position 7 to position 3
rotate right 3 steps
swap position 1 with position 2""".split("\n")


def swap_pos(cmd, string):
    # swap position 4 with position 0
    tokens = cmd.split(" ")
    pos2 = int(tokens[2])
    pos1 = int(tokens[-1])
    char1 = string[pos1]
    char2 = string[pos2]
    string[pos1] = char2
    string[pos2] = char1
    return string


def swap_letter(cmd, string):
    #swap letter f with letter g
    tokens = cmd.split(" ")
    letter2 = tokens[2]
    letter1 = tokens[-1]
    for i in range(0, len(string)):
        if string[i] == letter1:
            string[i] = letter2
        elif string[i] == letter2:
            string[i] = letter1
    return string


def rotate_right(cmd, string):
    #rotate left 6 steps
    tokens = cmd.split(" ")
    steps = int(tokens[-2])
    return string[steps:] + string[:steps]


def rotate_left(cmd, string):
    #rotate right 6 steps
    tokens = cmd.split(" ")
    steps = int(tokens[-2])
    return string[-steps:] + string[:-steps]


rotate_based_rev_map = {
    1: 0,
    3: 1,
    5: 2,
    7: 3,
    2: 4,
    4: 5,
    6: 6,
    0: 7
}

rotate_test_rev_map = {
    1: 0,
    3: 1,
    0: 2,
    2: 3,
    0: 4
}


def old_rotate_based(cmd, string):
    tokens = cmd.split(" ")
    char = tokens[-1]
    idx = int(string.index(char))
    string = string[-1:] + string[:-1]
    string = string[-idx:] + string[:-idx]
    if idx >= 4:
        string = string[-1:] + string[:-1]
    return string


def rotate_based(cmd, string):
    #rotate based on position of letter d
    tokens = cmd.split(" ")
    char = tokens[-1]
    idx = rotate_based_rev_map[int(string.index(char))]
    #idx = rotate_test_rev_map[int(string.index(char))]
    while string.index(char) != idx:
        string = rotate_left("rotate left 1 step", string)

    return string


def reverse_pos(cmd, string):
    #reverse positions 3 through 7
    tokens = cmd.split(" ")
    start = int(tokens[2])
    end = int(tokens[-1]) + 1
    subs = string[start:end]
    subs = subs[::-1]
    return string[:start] + subs + string[end:]


def move_pos(cmd, string):
    #move position 0 to position 4
    tokens = cmd.split(" ")
    posy = int(tokens[2])
    posx = int(tokens[-1])
    char = string[posx]
    del string[posx]
    string.insert(posy, char)
    return string


mapping = {
    "swap position": swap_pos,
    "swap letter": swap_letter,
    "rotate left": rotate_left,
    "rotate right": rotate_right,
    "rotate based on": rotate_based,
    "reverse positions": reverse_pos,
    "move position": move_pos,
}


def parse_op(line, string):
    for funcstr, func in mapping.items():
        if funcstr in line:
            return func(line, string)


def map_rotate_based():
    x = ["1", "2", "3", "4", "5", "6", "7", "8"]
    x = ["1", "2", "3", "4", "5"]
    for i in range(0, 9):
        y = old_rotate_based("rotate based on position of letter 1", x)
        print("POS", x.index("1"), "MOVE TO", y.index("1"))
        x = rotate_left("rotate left 1 step", x)

#map_rotate_based()
#import sys
#sys.exit(0)

line1 = "swap position 4 with position 0"
line2 = "swap letter d with letter b"
line3 = "reverse positions 0 through 4"
line4 = "rotate left 1 step"
line5 = "move position 1 to position 4"
line6 = "move position 3 to position 0"
line7 = "rotate based on position of letter b"
line8 = "rotate based on position of letter d"

basestr = ["d", "e", "c", "a", "b"]

#basestr = parse_op(line8, basestr)
#assert ''.join(basestr) == "ecabd"

#basestr = parse_op(line7, basestr)
#assert ''.join(basestr) == "abdec"

#basestr = parse_op(line6, basestr)
#assert ''.join(basestr) == "bdeac"

#basestr = parse_op(line5, basestr)
#assert ''.join(basestr) == "bcdea"

#basestr = parse_op(line4, basestr)
#assert ''.join(basestr) == "abcde"

#basestr = parse_op(line3, basestr)
#assert ''.join(basestr) == "edcba"

#basestr = parse_op(line2, basestr)
#assert ''.join(basestr) == "ebcda"

#basestr = parse_op(line1, basestr)
#assert ''.join(basestr) == "abcde"
#import sys
#sys.exit(0)

password = ["a", "b", "c", "d", "e", "f", "g", "h"]
password = ["f", "b", "g", "d", "c", "e", "a", "h"]

lenp = len(password)
for line in input[::-1]:
    password = parse_op(line, password)
    print(password)
    if password is None:
        print(line)
    assert len(password) == lenp
    print(password)