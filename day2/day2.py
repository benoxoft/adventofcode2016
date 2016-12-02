data = """RDRRDLRRUDRUUUULDDRDUULLDUULDURDDUDRULDLUDDRLRDUDDURRRRURDURLLRDRUUULDLLLURDRLLULLUULULLLDLLLRRURRLRDUULRURRUDRRDRLURLRURLLULRUURRUURDDLDRDLDLLUDUULLLUUUUDULLDRRUURLDURDDDDDRLLRRURDLUDRRUUDLRRLLRDURDUDDDLRDDRDLRULLUULRULRLLULDDRURUUDLDDULDRLLURDDUDDUDRDUDLDRRRDURRLDRDRLDLLDUDDDULULRRULRLLURDRRDDUUUUUULRUDLRRDURDLRDLUDLDURUDDUUURUDLUUULDLRDURDLDUUDLDDDURUUDUUDRLRDULLDUULUDRUDRLRRRDLLDRUDULRRUDDURLDRURRLLRRRDRLLDLULULRRUURRURLLUDRRLRULURLDDDDDURUDRRRRULLUUDLDDLUUL
ULURUDLULDULDLLDDLLLDRRLLUDRRDRDUDURUDLRRRRUDRDDURLRRULLDLURLDULLUDDLUDURDUURRRRLDLRLDDULLRURLULLDDRUDLRRRLDRRRDLDRLLDDRRDDLUUDRUDDLULRURLDURRLLDLRUDLLRRUULUDRLLLRLDULURRRRRDDUURDRRUUDULRUULDDULRLUDLUDDULLRLRDDLRLLURRRULDLRRRUURRLDDRDLRDLRRDRDLDRDUDRDURUUDRLRRULRDLLDLLRRRDRLDRLRLRLLLURURDULUUDDRLLDDDRURRURLRDDULLRURUDRRDRLRRRLDLRLRULDRLUURRUUULRLDLLURLLLDLLLDRRDULRURRRRLUDLLRRUDLRUDRURDRRDLUUURRDLRLRUUUDURDLUDURRUUDURLUDDDULLDRDLLDDDRLDDDRLDLDDDDUDUUDURUUDULRDDLULDRDRLURLUDRDLUULLULRLULRDDRULDUDDURUURULUDLUURLURU
URLURDDRLLURRRLDLDLUDUURDRUDLLLRRDLUUULRRLURRRLUDUDLRLDDRUDLRRRULUDUDLLLULULLLRUDULDDDLLLRRRLRURDULUDDDULDLULURRRDLURDLRLLDUDRUDURDRRURULDRDUDLLRDDDUDDURLUULLULRDRRLDDLDURLRRRLDRDLDULRULRRRLRLLDULRDLURLRUUDURRUUDLLUDRUDLRLDUUDLURRRDDUUDUDRLDLDDRURDDLLDDRDLRLRDLLLUDLUUDRLRLRDDRDLRDLLUULLLLUULLDLLDLRDLRLRRLUUDLLRLRUDRURULRLRLULUDRLLUDDUDDULRLDDRUUUURULDRRULLLDUURULUDRLLURLRRLDLRRLDDRRRDUDDUDLDDLULUDDUURDLLLRLDLRDRUUUUUDDDLDRDDRRRLRURRRRDURDRURUDLURRURDRLRUUDDLDRRULLDURDRLRRDURURUULRDUDLDRDDLULULRDRRUDDRLLRLULRLLUUDRDUUDDUDLRUUDLLUULLRUULUDDLURRRLLDRLRRLLRULLDUULURLLLLUUULDR
LDUURULLRLDRRUUDUUUURUUUDDDURRDDLRDLLRDDRULDDUURUDDURLLUDRDUDRDULDRRRLULUDRULLLLDRLLDRDLDLLRURULUDDDDURDDDRLLUDLDRULRDLDUDDDUUDLLRLLLDLRLRLRRUDDULDDDUDLDDLUDDULDLLLLULLLLDDURDDURRRDDRLRLLUDLLUDDDUDURUDRLRDRULULDDRULDLULULLRUULRLDULUURRDRDRRDLDDDRRLUULDLUDRDDUDLRURULLDDURLDDRULUDLDDDRDRLLRDLLUURRRURDRLRURLDDLURDRURDDURLLRLRUDUUDLDUDURRDDURDRDDUDDDUDUURURDDLLRUUDDRRDULDDLLDLRULUULRUUDLLDRLULDULDDUDLULRULDRLLDUULDDDLRLLRLULDDULDDRRRLDRRLURULRDDRDLRRDUDDRDRRRRUDUDLLRRDRRURRUURDRULDDUDURLUDDURDUDRDUULLDRURUURURDRRLDDLDLUURLULRUDURDRUUURRURRDRUDRUURDURLRULULLLULDLLDLRRLDRDLUULUDDDLRDRLRLDRUDUDRLLRL
LURLUURLURDUUDRUDLDLLURRRDLDRRRULDDRRDRDUUDRUDURDDDURLUDDLULUULRRLLRULUDRDDRRRLDURDUDDURDDDLRLDDLULLDRDDLUUDUURRRLULRUURRRRLLULDUDRDUURRRURRDRDUDUDLUDULLDLDDRLUDRURDULURLURRLLURLLLRLUURLRUDLUDDRLURRUULULRLURRURUDURDLDLDDUDDRDLLRLLRRULDDRUDURUDDDUDLLRDLRUDULLLRRRUURUDUUULLRDUDRURUDULLDLLUUUDRULRLLRRDDDDUDULDRDRLLDDLLDDDURRUDURLDLRDRUURDDURLRDRURLRRLLRLULDRRLRUDURDUURRLUUULUDDDLRLULRDRLLURRRDLURDUUDRRRLUURRLLUDLUDLUULLRRDLLRDDRURRUURLDDLRLRLRUDLDLRLRDRRDLLLRDLRDUDLLDDDRD"""

lines = data.split("\n")

example = """ULL
RRDDD
LURDL
UUUUD""".split("\n")

def map_pos_to_digit2(x, y):
    if x < 0 or y < 0:
        return 0

    digits = ((0, 0, 1, 0, 0,),
              (0, 2, 3, 4, 0,),
              (5, 6, 7, 8, 9,),
              (0, 10, 11, 12, 0,),
              (0, 0, 13, 0, 0,),)
    try:
        return digits[y][x]
    except:
        return 0


def map_pos_to_digit(x, y):
    digits = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 9))
    return digits[y][x]


def find_passcode(lines):
    x = 1
    y = 1
    passcode = []
    for line in lines:
        for c in line:
            if c == "R" and x < 2:
                x += 1
            elif c == "L" and x > 0:
                x -= 1
            elif c == "U" and y > 0:
                y -= 1
            elif c == "D" and y < 2:
                y += 1

        passcode.append(map_pos_to_digit(x, y))
    return passcode


def find_passcode2(lines):
    x = 0
    y = 2
    assert map_pos_to_digit2(x, y) == 5
    passcode = []
    for line in lines:
        for c in line:
            print(x,y)
            if c == "R" and map_pos_to_digit2(x+1, y) != 0:
                x += 1
            elif c == "L" and map_pos_to_digit2(x-1, y) != 0:
                x -= 1
            elif c == "U" and map_pos_to_digit2(x, y-1) != 0:
                print(map_pos_to_digit2(x, y-1))
                y -= 1
            elif c == "D" and map_pos_to_digit2(x, y+1) != 0:
                y += 1
        passcode.append(map_pos_to_digit2(x, y))
    return passcode

if __name__ == "__main__":
    assert map_pos_to_digit2(0, 2) == 5
    assert map_pos_to_digit2(0, 1) == 0
    assert map_pos_to_digit2(2, 0) == 1
    print(find_passcode(example))
    print(find_passcode(lines))
    print(find_passcode2(example))
    print(find_passcode2(lines))

