salt = b'ahsbgdzn'
#salt = b'abc'

MAX_LOOPS = 1000 * 1000 * 1000

import hashlib


def validate_hash(hash: str, consec: int) -> str:
    consecutives = []
    for i in range(0, len(hash) - (consec-1)):
        same = True
        for j in range(1, consec):
            if hash[i] != hash[i+j]:
                same = False
        if same:
            consecutives.append(hash[i])
    return consecutives


def find_keys():
    candidates = []
    elected = []

    for i in range(0, MAX_LOOPS):
        for candidate in candidates:
            if candidate[1] + 1000 < i:
                del candidates[0]
        m = hashlib.md5()
        m.update(salt + str.encode(str(i)))
        x = m.hexdigest()
        consecutives5 = validate_hash(x, 5)
        if len(consecutives5) > 0:
            for cc in consecutives5:
                for candidate in candidates:
                    if cc in candidate[2] and candidate not in elected:
                        print("found", candidate)
                        elected.append(candidate)
        consecutives3 = validate_hash(x, 3)
        if len(consecutives3) > 0:
            candidates.append((x, i, consecutives3))
        if len(elected) >= 100:
            return elected

#keys = find_keys()

def get_hash(tohash):
    m = hashlib.md5()
    m.update(tohash)
    tohash = m.hexdigest()
    for i in range(0, 2016):
        m = hashlib.md5()
        m.update(str.encode(tohash))
        tohash = m.hexdigest()
    return tohash

col = []
for i in range(0, MAX_LOOPS):
    m = hashlib.md5()
    x = get_hash(salt + str.encode(str(i)))
    letters = validate_hash(x, 3)
    for letter in letters:
        for j in range(i+1, i+1+1000):
            y = get_hash(salt + str.encode(str(j)))
            if letter in validate_hash(y, 5):
                col.append(i)
                print("FOUND", i, x, "WITH", j, y)
                break
        break
    if len(col) >= 64:
        break
print(col)
#print(sorted(keys, key=lambda x: x[1])[64])