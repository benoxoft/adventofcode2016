input = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."


def find_next_row(row):
    nextrow = ""
    for i in range(0, len(row)):
        nextrow += analyze_tile(row, i)
    return nextrow


def analyze_tile(row, index):
    if index == 0:
        left = "."
    else:
        left = row[index-1]
    center = row[index]
    if index == len(row) - 1:
        right = "."
    else:
        right = row[index+1]

    if left == "^" and center == "^" and right == ".":
        return "^"
    elif center == "^" and right == "^" and left == ".":
        return "^"
    elif left == "^" and center == "." and right == ".":
        return "^"
    elif left == "." and center == "." and right == "^":
        return "^"
    else:
        return "."


test1 = "..^^."
nextrow = find_next_row(test1)
assert nextrow == ".^^^^"
nextrow = find_next_row(nextrow)
assert nextrow == "^^..^"

test2 = """.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^""".split("\n")

currentrow = None
tile_count = 0
for row in test2:
    if currentrow is None:
        currentrow = row
        tile_count += currentrow.count(".")
        print(currentrow)
    else:
        nextrow = find_next_row(currentrow)
        tile_count += nextrow.count(".")
        print(nextrow)
        assert nextrow == row
        currentrow = nextrow
print(tile_count)

currentrow = input
tile_count = currentrow.count(".")
rows = []
rows.append(currentrow)
print(currentrow)
for i in range(0, 400000-1):
    nextrow = find_next_row(currentrow)
    currentrow = nextrow
    print(nextrow)
    tile_count += nextrow.count(".")
    rows.append(nextrow)
assert len(rows) == 400000
print(tile_count)