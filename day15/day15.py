class Disk:
    def __init__(self, total_positions, start_position):
        self._position = start_position
        self._total = total_positions

    def flip(self):
        self._position += 1
        if self._position == self._total:
            self._position = 0

    def get_position(self):
        return self._position


class Machine:

    def __init__(self):
        self.disks = []
        self._capsule_disk = None
        self.time = 0
        self.success = False

    def tick(self):
        self.time += 1
        for disk in self.disks:
            disk.flip()
        if self._capsule_disk and self._capsule_disk.get_position() == 0:
            next_capsule_id = self.disks.index(self._capsule_disk) + 1
            if next_capsule_id == len(self.disks):
                self.success = True
                return False
            self._capsule_disk = self.disks[next_capsule_id]
        else:
            self._capsule_disk = None
            return False

        return True

    def has_capsule(self):
        return self._capsule_disk

    def give_capsule(self):
        return self.success

    def drop_capsule(self):
        self._capsule_disk = self.disks[0]


import copy
modelmachine = Machine()


#Disc #1 has 13 positions; at time=0, it is at position 11.
#Disc #2 has 5 positions; at time=0, it is at position 0.
#Disc #3 has 17 positions; at time=0, it is at position 11.
#Disc #4 has 3 positions; at time=0, it is at position 0.
#Disc #5 has 7 positions; at time=0, it is at position 2.
#Disc #6 has 19 positions; at time=0, it is at position 17.
modelmachine.disks.append(Disk(13, 11))
modelmachine.disks.append(Disk(5, 0))
modelmachine.disks.append(Disk(17, 11))
modelmachine.disks.append(Disk(3, 0))
modelmachine.disks.append(Disk(7, 2))
modelmachine.disks.append(Disk(19, 17))
modelmachine.disks.append(Disk(11, 0))

#Disc #1 has 5 positions; at time=0, it is at position 4.
#Disc #2 has 2 positions; at time=0, it is at position 1.
#modelmachine.disks.append(Disk(5, 4))
#modelmachine.disks.append(Disk(2, 1))

while True:
    print(modelmachine.time)
    machine = copy.deepcopy(modelmachine)
    machine.drop_capsule()
    while machine.tick():
        continue
    if machine.give_capsule():
        print("Success!", modelmachine.time)
        break
    modelmachine.tick()
