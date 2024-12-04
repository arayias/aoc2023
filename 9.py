import math
from helper import read_file


def extrapolate(arr):
    extr = [arr]
    done = False
    while not done:
        curr = []
        z = 0
        for i in range(len(arr) - 1):
            calc = arr[i+1] - arr[i]
            curr.append(calc)
            if calc == 0:
                z += 1
        extr.append(curr)
        arr = curr
        if z == len(arr):
            done = True
    c = 0
    for i in extr:
        c += i[-1]
    return c


def extrapolate_backwards(arr):
    extr = [arr]
    done = False
    while not done:
        curr = []
        z = 0
        for i in range(len(arr) - 1):
            calc = arr[i+1] - arr[i]
            curr.append(calc)
            if calc == 0:
                z += 1
        extr.append(curr)
        arr = curr
        if z == len(arr):
            done = True
    c = 0
    for i in extr[::-1]:
        c = i[0] - c
    return c


def solve_p1():
    x = read_file(__file__).split('\n')
    x = list(map(lambda f: list(map(int, f.split())), x))
    a = 0
    for seq in x:
        a += extrapolate(seq)
    return a


def solve_p2():
    x = read_file(__file__).split('\n')
    x = list(map(lambda f: list(map(int, f.split())), x))
    a = 0
    for seq in x:
        a += extrapolate_backwards(seq)
    return a


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
