import hashlib

input = b"qtetzkpl"


class Room:
    def __init__(self, up=None, down=None, left=None, right=None):
        self.room_down = None
        self.room_up = None
        self.room_left = None
        self.room_right = None
        self.set_up(up)
        self.set_down(down)
        self.set_left(left)
        self.set_right(right)

    def unlock_doors(self, hash_input: str):
        m = hashlib.md5()
        m.update(hash_input)
        hash = m.hexdigest()

        unlocked = []
        if self.is_open(hash[0]) and self.room_up is not None:
            unlocked.append((self.room_up, hash_input + b"U"))
        if self.is_open(hash[1]) and self.room_down is not None:
            unlocked.append((self.room_down, hash_input + b"D"))
        if self.is_open(hash[2]) and self.room_left is not None:
            unlocked.append((self.room_left, hash_input + b"L"))
        if self.is_open(hash[3]) and self.room_right is not None:
            unlocked.append((self.room_right, hash_input + b"R"))
        return unlocked

    def set_left(self, room):
        if room is None:
            return
        if self.room_left is not None:
            return
        self.room_left = room
        self.room_left.set_right(self)

    def set_right(self, room):
        if room is None:
            return
        if self.room_right is not None:
            return
        self.room_right = room
        self.room_right.set_left(self)

    def set_up(self, room):
        if room is None:
            return
        if self.room_up is not None:
            return
        self.room_up = room
        self.room_up.set_down(self)

    def set_down(self, room):
        if room is None:
            return
        if self.room_down is not None:
            return
        self.room_down = room
        self.room_down.set_up(self)

    @staticmethod
    def is_open(char):
        return char in "bcdef"

room00 = Room()
room01 = Room(left=room00)
room02 = Room(left=room01)
room03 = Room(left=room02)
room10 = Room(up=room00)
room11 = Room(up=room01, left=room10)
room12 = Room(up=room02, left=room11)
room13 = Room(up=room03, left=room12)
room20 = Room(up=room10)
room21 = Room(up=room11, left=room20)
room22 = Room(up=room12, left=room21)
room23 = Room(up=room13, left=room22)
room30 = Room(up=room20)
room31 = Room(up=room21, left=room30)
room32 = Room(up=room22, left=room31)
room33 = Room(up=room23, left=room32)

assert room00.room_down == room10
assert room00.room_right == room01
assert room00.room_up is None
assert room00.room_left is None

assert room01.room_left == room00
assert room01.room_up is None
assert room01.room_right == room02
assert room01.room_down == room11

assert room02.room_left == room01
assert room02.room_up is None
assert room02.room_right == room03
assert room02.room_down == room12

assert room03.room_left == room02
assert room03.room_up is None
assert room03.room_right is None
assert room03.room_down == room13

assert room10.room_down == room20
assert room10.room_right == room11
assert room10.room_up == room00
assert room10.room_left is None

assert room11.room_left == room10
assert room11.room_up == room01
assert room11.room_right == room12
assert room11.room_down == room21

assert room12.room_left == room11
assert room12.room_up == room02
assert room12.room_right == room13
assert room12.room_down == room22

assert room13.room_left == room12
assert room13.room_up == room03
assert room13.room_right is None
assert room13.room_down == room23

assert room33.room_up == room23
assert room33.room_left == room32
assert room33.room_down is None
assert room33.room_right is None

#import sys
#sys.exit(0)

current: Room = room00
goal = room33

possibilities = current.unlock_doors(input)


def get_next_possibilities(possibilities, goal):
    new_possibilities = []
    for room, new_hash in possibilities:
        if room is goal:
            print(new_hash, len(new_hash))
            continue
        new_possibilities += room.unlock_doors(new_hash)
    return new_possibilities

#while True:
#    possibilities = get_next_possibilities(possibilities, goal)

def descend(room, hash, goal, hashes):
    for newroom, new_hash in room.unlock_doors(hash):
        if newroom is goal:
            for hh in hashes:
                if new_hash.startswith(hh):
                    raise Exception("impossible")
            hashes.append(new_hash)
            print(new_hash, len(new_hash))
            continue
        else:
            descend(newroom, new_hash, goal, hashes)

stack = []
hashes = []
stack += current.unlock_doors(input)
highest = 0
while True:
    if len(stack) == 0:
        break
    room, newhash = stack.pop()
    if len(newhash) > 5000:
        continue
    if room is goal:
        currentroom = current
        assert chr(newhash[-1]) in ("D", "R")
        print(len(newhash), newhash)
        if len(newhash) - 8 > highest:
            highest = len(newhash) - 8
        for i in range(8, len(newhash)):
            hash = newhash[i:i+1]
            if hash == b"D":
                currentroom = currentroom.room_down
            elif hash == b"U":
                currentroom = currentroom.room_up
            elif hash == b"L":
                currentroom = currentroom.room_left
            elif hash == b"R":
                currentroom = currentroom.room_right
            else:
                raise Exception("ERROR")
            if i == len(newhash) - 1:
                assert currentroom is goal
            else:
                assert currentroom is not goal
    else:
        stack += room.unlock_doors(newhash)

print(highest)