
rev = {
    "0": "1",
    "1": "0"
}


def fill_disk(data, disksize):
    while True:
        revstr = ''.join([rev[c] for c in data[::-1]])
        newstr: str = data + "0" + revstr
        if len(newstr) > disksize:
            return newstr[0:disksize]
        else:
            data = newstr


def find_checksum(data):
    checksum = ""
    for i in range(0, int(len(data)/2)):
        a, b = data[i*2:i*2+2]
        if a == b:
            checksum += "1"
        else:
            checksum += "0"
    if len(checksum) % 2 == 0:
        return find_checksum(checksum)
    else:
        return checksum

data = fill_disk("10000", 20)
print(data)
assert data == "10000011110010000111"
assert find_checksum("110010110100") == "100"


length = 35651584
input = "10111100110001111"
data = fill_disk(input, length)
checksum = find_checksum(data)
print(checksum)