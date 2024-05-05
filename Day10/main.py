# Standard library imports
import pathlib
import sys
import collections
import os

def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")

def next_part(pipes, pos, value):
    character = pipes[pos[0]][pos[1]]
    if value == 0:
        
    else:
        if character == "S":
            value += 1
            return value
        else:


def resolve_part1(pipes, posS):

    return None

def part1(lines):
    """Solve part 1."""
    pipes = []
    posS = [0, 0]
    for i in range(0,len(lines)):
        pipes.append([])
        j = 0
        for c in lines[i]:
            pipes[i].append(c)
            if c == "S":
                posS = [i, j]
            j += 1
    ##print(pipes[posS[0]][posS[1]])
            
    solution = resolve_part1(pipes, posS)
    return solution/2


def part2(lines):
    """Solve part 2."""
    return None


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