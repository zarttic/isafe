import utils


def fence(s):
    ss = utils.trim(s)
    for i in range(0, len(ss), 2):
        print(ss[i], end="")
    for i in range(1, len(ss), 2):
        print(ss[i], end="")


fence("meet me after the togo party".upper())
