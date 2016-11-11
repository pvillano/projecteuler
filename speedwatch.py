import math

import time

import sys


def lin(n):
    return n


def nlog2n(n):
    if n > sys.float_info.max ** (1 / 2.0): return math.inf
    return n * math.log2(n)


def square(n):
    return n * n


def cube(n):
    if n > sys.float_info.max ** (1 / 3.0): return math.inf
    return n ** 3


def exp(n):
    if n > 1023: return math.inf
    return 2.0 ** n


def fact(n):
    n = float(n)
    if n > 170: return math.inf
    return math.sqrt(2.0 * math.pi * n) * ((n / math.e) ** n)


def logfact(n):
    return 0.5 * math.log2(2 * math.pi * n) + n * math.log2(n) - n * math.log2(math.e)


def wordtime(t):
    if t < 1: return "{:.0f}ms".format(t * 1000)
    if t < 60: return "{:.0f}s".format(t)
    t /= 60
    if t < 60: return "{:.0f}m".format(t)
    t /= 60
    if t < 24: return "{:.0f}h".format(t)
    t /= 24
    if t < 7: return "{:.0f}d".format(t)
    t /= 7
    if t < 30.4: return "{:.0f}w".format(t / 7)
    if t < 365.2425: return "{:.0f}m".format(t / 30.4)
    t /= 365.2425
    if t < 100: return "{:.0f}y".format(t)
    if t < 1000: return "{:.0f}c".format(t / 100)
    if t < 1000000: return "{:.0f}M".format(t / 1000)
    return "inf"


def watch_time(solver, problems):
    algorithms = [lin, nlog2n, square, cube, exp, fact]
    for algorithm in algorithms:
        print("{:6}".format(algorithm.__name__), end=" ")
    print()
    for problem in problems:
        start = time.time()
        answer = solver(problem)
        stop = time.time()
        delta = stop - start
        for algorithm in algorithms:
            print("{:6}".format(wordtime((delta * algorithm(problems[-1]) / algorithm(problem)))), end=' ')
        print("| {:6} {}({})= {}".format(wordtime(delta), solver.__name__, problem, answer).ljust(40))
