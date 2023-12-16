# Standard library imports
import pathlib
import sys
import collections
import os

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

def cont_card_game(line):
    game, numbers = line.split(":")
    winning_numbers, playing_numbers = numbers.split("|")
    winning_numbers = winning_numbers.split(" ")
    playing_numbers = playing_numbers.split(" ")
    # Cleaning lists
    winning_numbers = [element for element in winning_numbers if element]
    playing_numbers = [element for element in playing_numbers if element]

    cont = 0
    for num in playing_numbers:
        if num in winning_numbers:
            cont += 1
    
    return cont

def card_game(line):
    cont = cont_card_game(line)
    if cont > 0:
        return 2**(cont-1)
    return 0

def card_game_copies(line, pos, copies):
    cont = cont_card_game(line)
    copy_line = copies[pos]
    for i in range(cont):
        pos_key = pos+i+1
        if pos_key in copies:
            copies[pos_key] += copy_line

    return copies

def part1(lines):
    """Solve part 1."""
    sum = 0
    for line, count in lines.items():
        sum += card_game(line)
    return sum


def part2(lines):
    """Solve part 2."""
    copies = {}
    for i in range(len(lines)):
        pos = i+1
        copies[pos] = 1

    i = 1
    for line, count in lines.items():
        copies = card_game_copies(line, i, copies)
        i += 1

    list_values = list(copies.values())
    return sum(list_values)

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