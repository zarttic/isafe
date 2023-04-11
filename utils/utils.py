# 去除空格
def trim(ss):
    s = ""
    for i in ss:
        if i.isalpha():
            s += i
    return s


def isp(n):
    fl = 1
    for i in range(2, n):
        if n % i == 0:
            fl = 0
            break

    return fl


def stoi(s):
    return ord(s) - ord('0')
