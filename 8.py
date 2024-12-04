import math
from helper import read_file
from collections import deque


def parse_nodes(arr):
    adj_dict = {}
    for entry in arr:
        start, lr = entry.split(" = ")
        l, r = lr[1:-1].split(", ")
        if entry not in adj_dict:
            adj_dict[start] = [l, r]
    return adj_dict


def solve_p1():
    x = read_file(__file__).split('\n')

    LEFT, RIGHT = 0, 1
    moves = x[0]
    nodes = parse_nodes(x[2:])

    current_node = "AAA"
    move_count = 0
    while current_node != "ZZZ":
        choice = LEFT if moves[move_count % len(moves)] == "L" else RIGHT
        current_node = nodes[current_node][choice]
        move_count += 1

    return move_count


def solve_p2():
    x = read_file(__file__).split('\n')

    LEFT, RIGHT = 0, 1
    moves = x[0]
    nodes = parse_nodes(x[2:])
    starting_nodes = deque()
    for k in nodes.keys():
        if k[-1] == "A":
            starting_nodes.append(k)

    move_count = 0
    terminations = []
    while starting_nodes:
        for _ in range(len(starting_nodes)):
            node = starting_nodes.popleft()
            choice = LEFT if moves[move_count %
                                   len(moves)] == "L" else RIGHT
            selected_node = nodes[node][choice]
            if selected_node[-1] == "Z":
                terminations.append(move_count + 1)
            else:
                starting_nodes.append(selected_node)
        move_count += 1
    return math.lcm(*terminations)


print(f"p1 : {solve_p1()}")
print(f"p2 : {solve_p2()}")
