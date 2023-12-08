# Standard library imports
import pathlib
import sys
import collections
import os

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

def is_valid_game(round, max_cubes):
    for cubes in round.split(","):
        if ("green" in cubes):
            if (int(cubes.strip(" green")) > max_cubes["green"]):
                return False
        if ("red" in cubes):
            if (int(cubes.strip(" red")) > max_cubes["red"]):
                return False
        if ("blue" in cubes):
            if (int(cubes.strip(" blue")) > max_cubes["blue"]):
                return False
    return True

def get_max_value(round, max_cubes):
    for cubes in round.split(","):
        if ("green" in cubes):
            if (int(cubes.strip(" green")) > max_cubes[0]):
                max_cubes[0] = int(cubes.strip(" green"))
        if ("red" in cubes):
            if (int(cubes.strip(" red")) > max_cubes[1]):
                max_cubes[1] = int(cubes.strip(" red"))
        if ("blue" in cubes):
            if (int(cubes.strip(" blue")) > max_cubes[2]):
                max_cubes[2] = int(cubes.strip(" blue"))

    return max_cubes

def part1(lines):
    """Solve part 1."""
    cubes = {"red" : 12, "green" : 13, "blue" : 14}
    sum = 0
    for line, count in lines.items():
        valid_game = True
        game, cube_sets = line.split(":")
        game = int(game.strip("Game "))
        for round in cube_sets.split(";"):
            if (not is_valid_game(round, cubes)):
                valid_game = False
                break
        if (valid_game):
            sum += game
    return sum


def part2(lines):
    """Solve part 2."""
    sum = 0
    for line, count in lines.items():
        valid_game = True
        game, cube_sets = line.split(":")
        game = int(game.strip("Game "))
        max_cubes = [0, 0, 0]
        for round in cube_sets.split(";"):
            max_cubes = get_max_value(round, max_cubes)
        result = 1
        for cube in max_cubes:
            result *= cube
        sum += result
    return sum


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