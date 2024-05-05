# Standard library imports
import pathlib
import sys
import collections
import os

def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")

def add_line_universe(lines):
    lines2 = list()
    for line in lines:
        galaxy = False
        j = 0
        while not galaxy and j < len(line):
            if (line[j] == "#"):
                galaxy = True
            j += 1

        lines2.append(line)
        if not galaxy:
            lines2.append(line)
    return lines2

def expand_universe(lines):
    i = 0
    for line in lines:
        line2 = list(line)
        lines[i] = line2
        i += 1

    lines2 = add_line_universe(lines)
    # Traspuesta
    lines2 = [list(col) for col in zip(*lines2)]
    new_universe = add_line_universe(lines2)
    # Traspuesta
    new_universe = [list(col) for col in zip(*new_universe)]

    return new_universe


def sum_pair(galaxy1, galaxy2):
    total = abs(galaxy1[0]-galaxy2[0])+abs(galaxy1[1]-galaxy2[1])
    return total

def resolve_part1(universe):
    galaxies = list()
    i = 0
    for line in universe:
        j = 0
        for c in line:
            if c == "#":
                galaxies.append([i, j])
            j += 1
        i += 1
    
    total_pair = 0
    i = 1
    for galaxy in galaxies:
        j = i
        while j < len(galaxies):
            total_pair += sum_pair(galaxy, galaxies[j])
            j += 1
        i += 1

    return total_pair

def resolve_part2(universe):
    #Brute force not possible
    return 0


def part1(lines):
    """Solve part 1."""
    total_pair = 0
    new_universe = expand_universe(lines)
    total_pair = resolve_part1(new_universe)
    return total_pair


def part2(lines):
    """Solve part 2."""
    total_pair = 0
    total_pair = resolve_part2(None)
    return total_pair


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