# Standard library imports
import pathlib
import sys
import collections
import os
from itertools import chain

def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")

def get_number(line, pos):
    c_number = ""
    number_back = False
    number_front = False

    if (line[pos].isnumeric()):
        c_number = line[pos]
        number_back = True
        number_front = True

    aux_pos = pos
    while number_back:
        try:
            if (line[aux_pos-1].isnumeric()):
                c_number = line[aux_pos-1]+c_number
                aux_pos -= 1
            else:
                number_back = False
        except:
            number_back = False

    aux_pos = pos
    while number_front:
        try:
            if (line[aux_pos+1].isnumeric()):
                c_number = c_number+line[aux_pos+1]
                aux_pos += 1
            else:
                number_front = False
        except:
            number_front = False

    if c_number == "":
        return 0

    return int(c_number)

def get_numbers_set(line, pos):
    set_numbers = set()
    if pos > 0:
        pos-=1
    for i in range(3):
        number = get_number(line, pos)
        pos+=1
        if (number != 0):
            set_numbers.add(number)

    return list(set_numbers)

def get_numbers(line1, line2, line3):
    list_numbers = []
    for i in range(len(line2)):
        if not line2[i].isalpha() and not line2[i].isnumeric() and line2[i] != ".":
            list_numbers.append(get_numbers_set(line1, i))
            list_numbers.append(get_numbers_set(line2, i))
            list_numbers.append(get_numbers_set(line3, i))

    #Reducir lista de listas
    list_numbers = list(chain(*list_numbers))

    return sum(list_numbers)

def get_numbers_gear(line1, line2, line3):
    list_numbers = []
    for i in range(len(line2)):
        gear_numbers = []
        if line2[i] == "*":
            gear_numbers.append(get_numbers_set(line1, i))
            gear_numbers.append(get_numbers_set(line2, i))
            gear_numbers.append(get_numbers_set(line3, i))
            gear_numbers = list(chain(*gear_numbers))
            if len(gear_numbers) >= 2:
                mult = 1
                for number in gear_numbers:
                    mult *= number
                list_numbers.append(mult)

    return sum(list_numbers)

def part1(lines):
    """Solve part 1."""
    sum = 0
    line_1 = None
    for i in range(len(lines)):
        if i < len(lines)-1:
            line_3 = lines[i+1]
        sum_line = get_numbers(line_1, lines[i], line_3)
        sum += sum_line
        line_1 = lines[i]
        line_3 = None
    return sum


def part2(lines):
    """Solve part 2."""
    sum = 0
    line_1 = None
    for i in range(len(lines)):
        if i < len(lines)-1:
            line_3 = lines[i+1]
        sum_line = get_numbers_gear(line_1, lines[i], line_3)
        sum += sum_line
        line_1 = lines[i]
        line_3 = None
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