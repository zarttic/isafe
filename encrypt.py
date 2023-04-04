import utils


def encrypt(row, col, ss, key=""):
    enstr = ""
    s = utils.trim(ss)
    sli = [["*" for _ in range(8)] for i in range(4)]
    if len(key) == 0:
        for i in range(col):
            key += chr(i + ord('1'))
    for i in range(len(key)):
        sli[0][i] = utils.stoi(key[i])
    for i in range(len(s)):
        sli[int(i / col) + 1][i % col] = s[i]
    for i in range(0, row + 1):
        print(sli[i])

    for i in range(1, col + 1):
        for j in range(col):
            if i == sli[0][j]:
                for z in range(row):
                    enstr += sli[z + 1][j]
                    if sli[z + 1][j] != "*":
                        print(sli[z + 1][j], end="")
                print("", end=" ")
                continue

    print("")
    return enstr


def decode(row, col, s, key):
    for i in range(0, row):
        for j in range(0, col):
            for z in range(0, col):
                if utils.stoi(key[z]) == j + 1:
                    if s[z*row+i] != '*':
                        print(s[z * row + i], end="")
                    break


# print(encrypt(3, 8, "meet me after the togo party"))
key = "34127856"
ss = encrypt(3, 8, "meet me after the togo party".upper())
s = encrypt(3, 8, "meet me after the togo party".upper(), key)
# decode(3, 8, ss, key)
