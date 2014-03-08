import matplotlib
matplotlib.use('Agg')

import sys
import pickle
import numpy as np
import pylab as P

def savefig(fn):
    def s(*ar, **kw):
        P.clf()
        fn(*ar, **kw)
        P.savefig(fn.__name__ + ".pdf", format="pdf", transparent=True,
                  bbox_inches="tight")
    return s

@savefig
def part_a(data):
    pos = np.arange(2)
    P.xticks(pos, ['Heads', 'Tails'])
    P.bar(pos, data, width=0.3, align='center')

@savefig
def part_b(data):
    hist_plot(data)

def p_c(data):
    n = len(data)
    P.gcf().set_size_inches(5, 20)
    for i in range(len(data)):
        P.subplot(n, 1, i+1)
        P.hist(data[i], 100, histtype='bar', rwidth=0.8)

@savefig
def part_c(data):
    p_c(data)

@savefig
def part_d(data):
    p_c(data)

def p_e(data):
    n = len(data)
    fig, axes = P.subplots(n, sharex=True)
    fig.set_size_inches(5, 20)
    for i in range(len(data)):
        axes[i].hist(data[i], 100, histtype='bar', rwidth=0.8)

@savefig
def part_e(data):
    p_e(data)

@savefig
def part_f(data):
    p_e(data)

def p_h(data):
    P.gcf().set_size_inches(10, 5)
    x = np.arange(1, len(data[0]) + 1, 1)
    for y in data:
        P.plot(x, y)
    P.ylabel("Number of heads - Number of tails")
    P.xlabel("Number of coin tosses")

@savefig
def part_h(data):
    p_h(data)

@savefig
def part_i(data):
    p_h(data)


def p_j(data):
    P.gcf().set_size_inches(10, 5)
    x = np.arange(1, len(data[0][1]) + 1, 1)
    for q, y in data:
        P.plot(x, y, ".", label="q = " + str(q))
    P.legend(loc="lower right")

@savefig
def part_j(data):
    p_j(data)
    P.ylabel("Frequency of heads less than $q$")
    P.xlabel("$k$")

@savefig
def part_k(data):
    p_j(data)
    P.yscale('log')
    P.ylabel("Frequency of heads less than $q$")
    P.xlabel("$k$")

@savefig
def part_l(data):
    x, y = data
    P.plot(x, y)
    P.ylabel("Fraction of $m$ runs where $R \leq q$")
    P.xlabel("$k$")

def p_m(data):
    for d in data:
        k, (x, y) = d
        P.plot(x, y, label="k = "+str(k))
    P.plot(x, y)
    P.legend(loc="lower right")

@savefig
def part_m(data):
    p_m(data)
    P.ylabel("Fraction of $m$ runs where $R \leq q$")
    P.xlabel("$k$")

@savefig
def part_n(data):
    x, ys = data
    q25, q50, q75 = zip(*ys)
    P.plot(x, q25, label = "25th Quartile")
    P.plot(x, q50, label = "50th Quartile")
    P.plot(x, q75, label = "75th Quartile")
    P.legend(loc="lower right")
    P.xscale('log')
    P.ylabel("Value of $q$ for quartile markers")
    P.xlabel("$k$")

@savefig
def part_o(data):
    x, ys = data
    gaps = [q75 - q25 for q25, _, q75 in ys]
    P.gcf().set_size_inches(5, 20)
    scales = (('linear', 'linear'), ('linear', 'log'),
              ('log', 'linear'), ('log', 'log'))
    for i, s in enumerate(scales):
        P.subplot(len(scales), 1, i+1)
        P.plot(x, gaps)
        P.xscale(s[0])
        P.yscale(s[1])
    P.ylabel("Gap between 0.25 and 0.75")
    P.xlabel("$k$")


@savefig
def part_p(data):
    P.gcf().set_size_inches(10, 5)
    p_m(data)
    P.ylabel("Fraction of $m$ runs where $R \leq q$")
    P.xlabel("Scaled $q$")

def hist_plot(data, bins=None):
    if bins is None:
        bins = np.arange(min(data), max(data), 1)
    P.hist(data, bins, histtype='bar', rwidth=0.8)

if __name__ == "__main__":
    data = pickle.load(open("data.pkl", 'rb'))
    if len(sys.argv) > 1:
        name = sys.argv[1]
        fn = globals()[name]
        fn(data[name])
    else:
        for key, val in sorted(globals().items()):
            if key.startswith("part"):
                val(data[key])
