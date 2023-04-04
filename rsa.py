import math
from utils import utils


# n e
def pub(p, q):
    n = p * q
    tem = (p - 1) * (q - 1)
    for i in range(2, tem):
        if utils.isp(i) == 1 and math.gcd(i, tem) == 1:
            return n, i


# n d
def pri(p, q, e=0):
    n = p * q
    if e == 0:
        n, e = pub(p, q)

    t = (p - 1) * (q - 1)
    for i in range(2, n):
        if (i * e) % t == 1:
            return n, i


def encode(m, p, q, e=0):
    n = p * q
    if e == 0:
        n, e = pub(p, q)
    return pow(m, e) % n


def decode(c, p, q, e=0):
    n, d = pri(p, q, e)
    return pow(c, d) % n


p = 7
q = 17
m = 19
print(pub(p, q))
print(pri(p, q))

print(encode(m, p, q))
print(decode(encode(m, p, q), p, q))
# print(pub(5, 17))
