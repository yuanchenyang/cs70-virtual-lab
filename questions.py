import sys
from utils import *
from random import random
from math import sqrt

PICKLE_FILENAME = "data.pkl"

def coin(heads=1, tails=0):
    if random() >= 0.5:
        return heads
    return tails

def p_a(k):
    heads = sum(coin() for _ in xrange(k))
    tails = k - heads
    return heads, tails

@write
def part_a():
    return p_a(1000)

def p_b(k, n):
    return [p_a(k)[0] for _ in xrange(n)]

@write
def part_b():
    return p_b(1000, 1000)

@write
def part_c():
    return [p_b(k, 1000) for k in (2, 4 ,10, 50, 100, 500, 10000, 100000)]

def p_d():
    return[map(lambda f: f - k // 2, p_b(k, 1000))
            for k in (2, 4 ,10, 50, 100, 500, 10000, 100000)]

@write
def part_d():
    return p_d()

@write
def part_e():
    return get_cached("part_d", p_d)

@write
def part_f():
    return [map(lambda f: (f - k / 2.0) / (k / 2.0), p_b(k, 1000))
            for k in (2, 4 ,10, 50, 100, 500, 10000, 100000)]

def p_h(k):
    cur = 0
    for _ in xrange(k):
        yield cur
        cur += coin(1, -1)

@write
def part_h():
    return [list(p_h(1000)) for _ in xrange(20)]


def p_i(k):
    for i, num in enumerate(p_h(k)):
        yield (num * 1.0) / (i + 1)

@write
def part_i():
    return [list(p_i(1000)) for _ in xrange(100)]

def p_j(k, m, q):
    lst = [0 for _ in xrange(m)]
    def roll(lst):
        for i in xrange(len(lst)):
            lst[i] += coin()

    for i in xrange(1, 1 + k):
        roll(lst)
        count = sum(1 for x in lst if x / (1.0 * i) <= q)
        yield (count * 1.0) / m

def p_j_2():
    qs = (0.1, 0.25, 0.4, 0.5)
    return [(q, list(p_j(1000, 10000, q))) for q in qs]

@write
def part_j():
    return p_j_2()

@write
def part_k():
    return get_cached("part_j", p_j_2)


def p_l(k, m):
    lst = sorted(sum(coin() for _ in xrange(k)) * 1.0 / k
                            for _ in xrange(m))
    q = [i/1000. for i in range(1000)]
    fracs = []
    li = 0
    for i, n in enumerate(q):
        try:
            while lst[li] <= n:
                li += 1
            fracs.append(li * 1.0 / m)
        except IndexError:
            fracs.append(1.0)
    return q, fracs

@write
def part_l():
    return p_l(1000, 10000)

def p_m():
    ks = (2, 10, 50, 100, 500, 10000, 100000)
    return [(k, p_l(k, 10000)) for k in ks]

@write
def part_m():
    return p_m()

def get_quartile_markers(x, y):
    markers = []
    for marker in (0.25, 0.5, 0.75):
        i = 0
        while y[i] < marker:
            i += 1
        markers.append(x[i])
    return markers

def p_n():
    d = get_cached("part_m", p_m)
    res = []
    for di in d[1:]: # k = 2 is not nice
        k, (x, y) = di
        res.append((k, get_quartile_markers(x, y)))
    return zip(*res)

@write
def part_n():
    return p_n()

@write
def part_o():
    return get_cached("part_n", p_n)

@write
def part_p():
    m = get_cached("part_m", p_m)
    res = []
    for k, pl in m:
        qs, fracs = pl
        res.append((k, ([(i - 0.5) * sqrt(k) + 0.5 for i in qs], fracs)))
    return res

if __name__ == "__main__":
    w = make_writer(PICKLE_FILENAME)
    if len(sys.argv) > 1:
        globals()[sys.argv[1]](w)
    else:
        for key, val in sorted(globals().items()):
            if key.startswith("part"):
                val(w)
