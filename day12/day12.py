data = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 17 c
cpy 18 d
inc a
dec d
jnz d -2
dec c
jnz c -5""".split("\n")

example = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""".split("\n")

x = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0,
    'p': 0
    }


def inc(reg):
    x[reg] += 1


def dec(reg):
    x[reg] -= 1


def cpy(val, reg):
    if val in x.keys():
        x[reg] = x[val]
    else:
        x[reg] = int(val)


def jnz(reg, val):
    if reg in x.keys():
        if x[reg] != 0:
            x['p'] += int(val)-1
    elif int(reg) != 0:
        x['p'] += int(val)-1

y = {
    'inc': inc,
    'dec': dec,
    'cpy': cpy,
    'jnz': jnz
}


def execute(data):
    while x['p'] < len(data):
        line = data[x['p']]
        tokens = line.split(" ")
        y[tokens[0]](*tokens[1:])
        x['p'] += 1
        print(x)

execute(data)
print(x)
