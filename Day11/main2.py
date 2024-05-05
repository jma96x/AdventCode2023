# Standard library imports
import pathlib
import sys
import collections
import os

def calc(values, mode):
    import itertools
    from grid import Grid

    grid = Grid.from_text(values)

    empty_col = set(x for x in grid.x_range() if set(grid.column(x)) == {"."})
    empty_row = set(y for y in grid.y_range() if set(grid.row(y)) == {"."})
    
    stars = [pt for pt, val in grid.grid.items() if val == "#"]
    range_sets = {}

    def get_range_set(a, b):
        ret = range_sets.get((a, b), None)
        if ret is None:
            ret = set(range(a, b))
            range_sets[(a, b)] = ret
        return ret

    ret = 0
    mult = 1 if mode == 1 else (1000000 - 1)
    for (ax, ay), (bx, by) in itertools.combinations(stars, 2):
        ax, bx = min(ax, bx), max(ax, bx)
        ay, by = min(ay, by), max(ay, by)

        ret += (bx - ax) + len(empty_col & get_range_set(ax, bx + 1)) * mult
        ret += (by - ay) + len(empty_row & get_range_set(ay, by + 1)) * mult

    return ret

def resolve_part2(universe):
    #Brute force not possible
    return 0


def part1(lines):
    """Solve part 1."""
    total_pair = calc(lines, 1)
    return total_pair


def part2(lines):
    """Solve part 2."""
    total_pair = calc(lines, 2)
    return total_pair


def solve(part, puzzle_input):
    """Solve the puzzle for the given input."""
    return part(puzzle_input)

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