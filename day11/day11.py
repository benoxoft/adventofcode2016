

class Material:

    def __init__(self, material_name: str):
        self._material_name = material_name

    def __str__(self):
        return self._material_name


class Type:
    def __init__(self, t: str):
        self._type = t

    def __str__(self):
        return self._type


class Item:

    def __init__(self, material: Material, type: Type):
        self._material = material
        self._type = type
        self._connected = None

    def get_material(self) -> Material:
        return self._material

    def get_type(self) -> Type:
        return self._type

    def connect(self, i) -> bool:
        if i.get_material() == self.get_material() and i.get_type() != self.get_type():
            self._connected = i
            return True
        return False

    def fry_item(self, i) -> bool:
        if self.get_type() == i.get_type():
            return False
        elif self.get_material() == i.get_material():
            return False
        elif self.connected():
            return False
        elif i.connected():
            return False
        else:
            return True

    def disconnect(self):
        self._connected = None

    def connected(self) -> bool:
        return self._connected is not None

    def __str__(self):
        return str(self.get_material()) + str(self.get_type())


class Microchip(Item):

    def __init__(self, material: Material, type: Type):
        super(Microchip, self).__init__(material, type)


class Generator(Item):

    def __init__(self, material: Material, type: Type):
        super(Generator, self).__init__(material, type)


class Platform:

    def __init__(self, maxitems: int):
        self._items = list()
        self._maxitems = maxitems

    def disconnect_all(self):
        for i in self._items:
            i.disconnect()

    def connect_all(self):
        for i in self._items:
            for j in self._items:
                i.connect(j)
                j.connect(i)

    def get_items(self) -> list:
        return self._items

    def add_item(self, newitem: Item) -> bool:
        if self._maxitems <= len(self._items):
            return False
        self._items.append(newitem)
        return True

    def transfer_item(self, item: Item, pf) -> bool:
        if not item in self._items:
            return False
        if pf.add_item(item):
            self._items.remove(item)
            return True
        else:
            return False


class Floor(Platform):
    def __init__(self, number: int):
        super(Floor, self).__init__(99)
        self._number = number

    def get_number(self) -> int:
        return self._number

    def __str__(self):
        s = "F" + str(self._number) + ": "
        for i in self.get_items():
            s += str(i) + " "
        return s


class Elevator(Platform):
    def __init__(self):
        super(Elevator, self).__init__(2)
        self._floors = dict()
        self._current_floor = None
        self._steps = 0

    def get_current_floor(self) -> Floor:
        return self._current_floor

    def get(self, item: Item) -> bool:
        return self._current_floor.transfer_item(item, self)

    def put(self, item: Item) -> bool:
        return self.transfer_item(item, self._current_floor)

    def __str__(self):
        s = ""
        for f in sorted(self._floors.values(), key=lambda x: -x.get_number()):
            if f == self._current_floor:
                s += "E " + str(f)
                for i in self.get_items():
                    s += str(i) + "(E) "
                s += "\n"
            else:
                s += "  " + str(f) + "\n"
        s += "steps: " + str(self._steps) + "\n"
        return s

    def add_floor(self, f: Floor):
        self._floors[f.get_number()] = f
        if self._current_floor is None:
            self._current_floor = self._floors[1]

    def move_up(self) -> bool:
        if len(self.get_items()) == 0:
            return False
        if self._current_floor.get_number() == len(self._floors):
            return False
        if self.check_floor(self._floors[self._current_floor.get_number()+1]):
            self._current_floor = self._floors[self._current_floor.get_number()+1]
            self._steps += 1
            print(self)
            return True
        else:
            return False

    def move_down(self) -> bool:
        if len(self.get_items()) == 0:
            return False
        if self._current_floor.get_number() == 1:
            return False
        if self.check_floor(self._floors[self._current_floor.get_number()-1]):
            self._current_floor = self._floors[self._current_floor.get_number()-1]
            self._steps += 1
            print(self)
            return True
        else:
            return False

    def check_floor(self, floor: Floor) -> bool:
        self.disconnect_all()
        floor.disconnect_all()
        self.connect_all()
        floor.connect_all()
        for eitem in self.get_items():
            for fitem in floor.get_items():
                eitem.connect(fitem)
                fitem.connect(eitem)
        for eitem in self.get_items():
            for fitem in floor.get_items():
                if eitem.fry_item(fitem):
                    return False
        return True



def execute_base_system1():
    pr = Material("Pr")
    ru = Material("Ru")
    pl = Material("Pl")
    st = Material("St")
    th = Material("Th")

    microchip = Type("M")
    generator = Type("G")

    prg = Generator(pr, generator)
    rug = Generator(ru, generator)
    plg = Generator(pl, generator)
    stg = Generator(st, generator)
    thg = Generator(th, generator)

    prm = Microchip(pr, microchip)
    rum = Microchip(ru, microchip)
    plm = Microchip(pl, microchip)
    stm = Microchip(st, microchip)
    thm = Microchip(th, microchip)

    #The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
    f1 = Floor(1)
    assert f1.add_item(thg)
    assert f1.add_item(thm)
    assert f1.add_item(plg)
    assert f1.add_item(stg)

    # The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
    f2 = Floor(2)
    assert f2.add_item(plm)
    assert f2.add_item(stm)

    # The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
    f3 = Floor(3)
    assert f3.add_item(prg)
    assert f3.add_item(prm)
    assert f3.add_item(rug)
    assert f3.add_item(rum)

    # The fourth floor contains nothing relevant.
    f4 = Floor(4)
    e = Elevator()
    e.add_floor(f1)
    e.add_floor(f2)
    e.add_floor(f3)
    e.add_floor(f4)
    print(e)

    assert e.get(plg)
    assert e.get(stg)
    assert e.move_up()
    assert e.move_up()
    assert e.put(plg)
    assert e.put(stg)
    assert e.get(rum)
    assert e.move_down()
    assert e.get(stm)
    assert e.move_up()
    assert e.put(rum)
    assert e.move_down()
    assert e.get(plm)
    assert e.move_up()
    assert e.put(plm)
    assert e.move_down()
    assert e.move_down()
    assert e.get(thm)
    assert e.move_up()
    assert e.move_up()
    assert e.put(stm)
    assert e.put(thm)
    assert e.get(prg)
    assert e.move_down()
    assert e.move_down()
    assert e.get(thg)
    assert e.move_up()
    assert e.move_up()
    assert e.move_up()
    assert e.put(prg)
    assert e.move_down()
    assert e.get(rug)
    assert e.move_up()
    assert e.put(rug)
    assert e.move_down()
    assert e.get(plg)
    assert e.move_up()
    assert e.put(plg)
    assert e.move_down()
    assert e.get(stg)
    assert e.move_up()
    assert e.put(stg)
    assert e.move_down()
    assert e.get(thm)
    assert e.move_up()
    assert e.put(thm)
    assert e.put(thg)
    assert e.get(prg)
    assert e.move_down()
    assert e.get(prm)
    assert e.move_up()
    assert e.put(prm)
    assert e.put(prg)
    assert e.get(rug)
    assert e.move_down()
    assert e.get(rum)
    assert e.move_up()
    assert e.put(rug)
    assert e.put(rum)
    assert e.get(plg)
    assert e.move_down()
    assert e.get(plm)
    assert e.move_up()
    assert e.put(plm)
    assert e.put(plg)
    assert e.get(stg)
    assert e.move_down()
    assert e.get(stm)
    assert e.move_up()


def execute_base_system2():
    pr = Material("Pr")
    ru = Material("Ru")
    pl = Material("Pl")
    st = Material("St")
    th = Material("Th")
    el = Material("El")
    di = Material("Di")
    microchip = Type("M")
    generator = Type("G")

    prg = Generator(pr, generator)
    rug = Generator(ru, generator)
    plg = Generator(pl, generator)
    stg = Generator(st, generator)
    thg = Generator(th, generator)
    elg = Generator(el, generator)
    dig = Generator(di, generator)

    prm = Microchip(pr, microchip)
    rum = Microchip(ru, microchip)
    plm = Microchip(pl, microchip)
    stm = Microchip(st, microchip)
    thm = Microchip(th, microchip)
    elm = Microchip(el, microchip)
    dim = Microchip(di, microchip)

    #The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
    f1 = Floor(1)
    assert f1.add_item(thg)
    assert f1.add_item(thm)
    assert f1.add_item(plg)
    assert f1.add_item(stg)
    assert f1.add_item(elg)
    assert f1.add_item(elm)
    assert f1.add_item(dig)
    assert f1.add_item(dim)

    # The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
    f2 = Floor(2)
    assert f2.add_item(plm)
    assert f2.add_item(stm)

    # The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
    f3 = Floor(3)
    assert f3.add_item(prg)
    assert f3.add_item(prm)
    assert f3.add_item(rug)
    assert f3.add_item(rum)

    # The fourth floor contains nothing relevant.
    f4 = Floor(4)
    e = Elevator()
    e.add_floor(f1)
    e.add_floor(f2)
    e.add_floor(f3)
    e.add_floor(f4)
    print(e)
    assert e.get(plg)
    assert e.get(stg)
    assert e.move_up()
    assert e.put(plg)
    assert e.put(stg)
    assert e.get(plm)
    assert e.move_down()
    assert e.get(dim)
    assert e.move_up()
    assert e.put(dim)
    assert e.put(plm)
    assert e.get(plg)
    assert e.move_down()
    assert e.get(dig)
    assert e.move_up()
    assert e.put(dig)
    assert e.move_down()
    assert e.get(elg)
    assert e.move_up()
    assert e.put(elg)
    assert e.put(plg)
    assert e.get(stm)
    assert e.move_down()
    assert e.get(elm)
    assert e.move_up()
    assert e.put(elm)
    assert e.move_down()
    assert e.get(thm)
    assert e.move_up()
    assert e.put(stm)
    assert e.put(thm)
    assert e.get(stg)
    assert e.move_down()
    assert e.get(thg)
    assert e.move_up()
    assert e.put(stg)
    assert e.put(thg)
    assert e.get(dim)
    assert e.get(dig)
    assert e.move_up()
    assert e.put(dim)
    assert e.move_down()
    assert e.get(thg)
    assert e.move_up()
    assert e.put(dig)
    assert e.put(thg)
    assert e.get(prm)
    assert e.move_down()
    assert e.get(thm)
    assert e.move_up()
    assert e.put(thm)
    assert e.move_down()
    assert e.get(stm)
    assert e.move_up()
    assert e.put(stm)
    assert e.put(prm)
    assert e.get(prg)
    assert e.move_down()
    assert e.get(stg)
    assert e.move_up()
    assert e.put(stg)
    assert e.move_down()
    assert e.get(plg)
    assert e.move_up()
    assert e.put(plg)
    assert e.put(prg)
    assert e.get(rum)
    assert e.move_down()
    assert e.get(plm)
    assert e.move_up()
    assert e.put(plm)
    assert e.move_down()
    assert e.get(elm)
    assert e.move_up()
    assert e.put(elm)
    assert e.put(rum)
    assert e.get(rug)
    assert e.move_down()
    assert e.get(elg)
    assert e.move_up()
    assert e.put(rug)
    assert e.get(elm)
    assert e.move_up()
    assert e.put(elm)
    assert e.move_down()
    assert e.get(dig)
    assert e.move_up()
    assert e.put(elg)
    assert e.move_down()
    assert e.get(dim)
    assert e.move_up()
    assert e.put(dim)
    assert e.move_down()
    assert e.get(rug)
    assert e.move_up()
    assert e.put(dig)
    assert e.move_down()
    assert e.get(rum)
    assert e.move_up()
    assert e.put(rug)
    assert e.move_down()
    assert e.get(plm)
    assert e.move_up()
    assert e.put(rum)
    assert e.move_down()
    assert e.get(plg)
    assert e.move_up()
    assert e.put(plg)
    assert e.move_down()
    assert e.get(prm)
    assert e.move_up()
    assert e.put(plm)
    assert e.move_down()
    assert e.get(prg)
    assert e.move_up()
    assert e.put(prg)
    assert e.move_down()
    assert e.get(stm)
    assert e.move_up()
    assert e.put(prm)
    assert e.move_down()
    assert e.get(stg)
    assert e.move_up()
    assert e.put(stg)
    assert e.move_down()
    assert e.get(thm)
    assert e.move_up()
    assert e.put(stm)
    assert e.move_down()
    assert e.get(thg)
    assert e.move_up()


def test_system():
    hy = Material("Hy")
    li = Material("Li")
    microchip = Type("M")
    generator = Type("G")
    hyg = Generator(hy, generator)
    lig = Generator(li, generator)
    hym = Microchip(hy, microchip)
    lim = Microchip(li, microchip)
    #The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
    f1 = Floor(1)
    assert f1.add_item(hym)
    assert f1.add_item(lim)

    #The second floor contains a hydrogen generator.
    f2 = Floor(2)
    assert f2.add_item(hyg)

    #The third floor contains a lithium generator.
    f3 = Floor(3)
    assert f3.add_item(lig)

    #The fourth floor contains nothing relevant.
    f4 = Floor(4)

    e = Elevator()
    e.add_floor(f1)
    e.add_floor(f2)
    e.add_floor(f3)
    e.add_floor(f4)

    print(e)
    #Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:
    assert e.get(hym)
    assert e.move_up()
    assert e.put(hym)
    print(e)
    assert e.get(hyg)
    assert e.get(hym)
    assert e.move_up()
    assert e.put(hyg)
    print(e)
    assert e.move_down()
    print(e)
    assert e.move_down()
    assert e.get(lim)
    print(e)
    assert e.move_up()
    print(e)
    assert e.move_up()
    print(e)
    assert e.move_up()
    print(e)
    assert e.put(lim)
    assert e.move_down()
    print(e)
    assert e.put(hym)
    assert e.get(lig)
    assert e.get(hyg)
    assert e.move_up()
    print(e)
    assert e.put(lig)
    assert e.put(hyg)
    assert e.get(lim)
    assert e.move_down()
    print(e)
    assert e.get(hym)
    assert e.move_up()
    print(e)
test_system()
execute_base_system2()
