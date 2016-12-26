import math

input = 3014603

class Elf:
    def __init__(self, number):
        self.left = None
        self.right = None
        self.gifts = 1
        self.number = number

    def set_left_elf(self, elf):
        if self.left is not None:
            return
        self.left = elf
        elf.set_right_elf(self)

    def set_right_elf(self, elf):
        if self.right is not None:
            return
        self.right = elf
        elf.set_left_elf(self)

    def give_gifts(self):
        return self.gifts

    def steal_gifts(self):
        self.gifts += self.right.gifts
        self.right = self.right.right
        return self.right

    def __str__(self):
        return str(self.number)

def create_elf_chain(amount):
    first = Elf(1)
    current = first
    for i in range(1, amount):
        next = Elf(i + 1)
        current.set_right_elf(next)
        current = next
    current.set_right_elf(first)
    return first


def match_elf_chain(first: Elf):
    elves = []
    next = first.right
    elves.append(first)
    while next != first:
        elves.append(next)
        next = next.right
    return elves


elf = create_elf_chain(input)
elves = match_elf_chain(elf)
total = len(elves)
front = math.floor(total / 2)
stolen = elf
for i in range(0, front):
    stolen = stolen.right
while elf.right != elf:
    if total % 1000 == 0:
        print(total)
    elf.gifts += stolen.gifts
    stolen.right.left = stolen.left
    stolen.left.right = stolen.right
    elf = elf.right
    stolen = stolen.right
    if total % 2 != 0:
        stolen = stolen.right
    total -= 1
print(elf.number, elf.gifts)



while len(elves) > 1:
    break
    if len(elves) % 1000 == 0:
        print(len(elves))
    x = elves.index(elf)
    if x + 1 > math.floor(len(elves) / 2):
        front_idx = x - math.floor(len(elves) / 2) - 1
    elif x + 1 == math.floor(len(elves) / 2):
        front_idx = math.floor(len(elves) / 2) + 1
        if front_idx >= len(elves):
            front_idx = len(elves) - 1
    else:
        front_idx = math.floor(len(elves) / 2) + x
    stolen = elves[front_idx]
    del elves[front_idx]
    elf.gifts += stolen.gifts
    if len(elves) <= x or len(elves) == 1:
        elf = elves[0]
    else:
        elf = elves[x+1]

#print(elves[0].number, elves[0].gifts)

while True:
    break
    elf = elf.steal_gifts()
    if elf.gifts == input:
        print(elf.number)
        break

