# Standard library imports
import pathlib
import sys
import collections
import os
import math

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

def solve_part1(instructions, paths):
    actual_path = "AAA"
    max_instructions = len(instructions)
    i = 0
    cont = 0
    while (actual_path != "ZZZ"):
        if (instructions[i] == "L"):
            actual_path = paths[actual_path][0]
        else:
            actual_path = paths[actual_path][1]
        if i == max_instructions-1:
            i = 0
        else:
            i += 1
        cont += 1

    return cont

##BRUTE FORCE, ... BAD SOLUTION
"""def solve_part2(instructions, paths):
    actual_paths = []
    for path in paths:
        if path[2] == "A":
            actual_paths.append(path)

    max_instructions = len(instructions)
    i = 0
    cont = 0

    while not all(value[2] == "Z" for value in actual_paths):
        i_path = 0
        for path in actual_paths:
            if (instructions[i] == "L"):
                actual_paths[i_path] = paths[path][0]
            else:
                actual_paths[i_path] = paths[path][1]
            i_path += 1

        if i == max_instructions-1:
            i = 0
        else:
            i += 1

        cont += 1
        #print(actual_paths)

    return cont"""

def solve_part2(instructions, paths):
    actual_paths = []
    for path in paths:
        if path[2] == "A":
            actual_paths.append(path)

    max_instructions = len(instructions)

    times = []
    path_i = 0
    for path in actual_paths:
        idx = 0
        cont = 0

        while path[2] != "Z":
            path = paths[path][0 if instructions[idx%max_instructions] == 'L' else 1]
            cont += 1
            #Only if the second loop is diferent, don't work because is cycle loop, then solution is more easier
            """if path[2] == "Z":
                if first_loop:
                    times[path_i][1] = cont
                    second_loop = True
                else:
                    first_loop = True
                    times.append([cont, 0])
                    cont = 0"""
            #print(actual_paths)
            idx += 1

        times.append(cont)

        path_i += 1

    lcm = math.lcm(*times)

    return lcm

def part1(lines):
    """Solve part 1."""
    instructions = ""
    paths = {}
    i = 0
    for line, count in lines.items():
        if i == 0:
            instructions = line
        elif i > 1:
            path = line.split(" = ")
            lrpath = path[1].rstrip(")").lstrip("(")
            lrpath = lrpath.split(", ")
            paths[path[0]] = [lrpath[0], lrpath[1]]
        i += 1

    cont = solve_part1(instructions, paths)

    return cont


def part2(lines):
    """Solve part 2."""
    instructions = ""
    paths = {}
    i = 0
    for line, count in lines.items():
        if i == 0:
            instructions = line
        elif i > 1:
            path = line.split(" = ")
            lrpath = path[1].rstrip(")").lstrip("(")
            lrpath = lrpath.split(", ")
            paths[path[0]] = [lrpath[0], lrpath[1]]
        i += 1

    cont = solve_part2(instructions, paths)

    return cont


def solve(part, puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    return part(data)

if __name__ == "__main__":
    path1 = "inputs/part1.txt"
    if os.path.exists(path1):
        print(f"\nPart1:")
        solution = solve(part1, puzzle_input=pathlib.Path(path1).read_text().strip())
        print(str(solution))
    path2 = "inputs/part2.txt"
    if os.path.exists(path2):
        print(f"\nPart2:")
        solution = solve(part2, puzzle_input=pathlib.Path(path2).read_text().strip())
        print(str(solution))
    else:
        print(f"\nPart2:")
        solution = solve(part2, puzzle_input=pathlib.Path(path1).read_text().strip())
        print(str(solution))