# Standard library imports
import pathlib
import sys
import collections
import os

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

def part1(rounds):
    """Solve part 1."""
    return None


def part2(rounds):
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