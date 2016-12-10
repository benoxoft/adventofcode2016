import hashlib

MAX_LOOPS = 1000 * 1000 * 1000

input = b"wtnhxymk"
password = ['','','','','','','','',]

for i in range(0, MAX_LOOPS):
    m = hashlib.md5()
    m.update(input + str.encode(str(i)))
    x = m.hexdigest()
    if x[0:5] == "00000":
        try:
            pos = int(x[5:6])
        except:
            continue
        if 0 <= pos <= 7 and password[pos] == '':
            password[pos] = x[6:7]
            print(password)
        if not '' in password:
            break

print(password)