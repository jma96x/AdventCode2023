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
    sum = 0
    for round, count in rounds.items():
        first_number = 0; last_number = 0
        for c in round:
            if c.isnumeric():
                if first_number == 0:
                    first_number = int(c)
                last_number = int(c)
        sum += int(str(first_number)+str(last_number))

    return sum


def part2(rounds):
    """Solve part 2."""
    numbers = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9,
               "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9 
               }

    sum = 0
    for round, count in rounds.items():
        first_indexs = {}
        last_indexs = {}
        for number in numbers:
            first_indexs[number] = round.find(number)
            last_indexs[number] = round.rfind(number)

        # Eliminar las claves cuyo valor es -1
        first_indexs_1 = {clave: valor for clave, valor in first_indexs.items() if valor != -1}
        #
        index_min_value = min(first_indexs_1, key=first_indexs_1.get)
        #
        index_max_value = max(last_indexs, key=last_indexs.get)

        sum += int(str(numbers[index_min_value])+str(numbers[index_max_value]))

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