# Standard library imports
import pathlib
import sys
import collections
import os
from functools import cmp_to_key

STRENGHT = {"A" : 1, "K" : 2, "Q" : 3, "J" : 4, "T" : 5, "9" : 6, "8" : 7, "7" : 8, "6" : 9, "5" : 10, "4" : 11, "3" : 12, "2" : 13}
STRENGHT_2 = {"A" : 1, "K" : 2, "Q" : 3, "T" : 4, "9" : 5, "8" : 6, "7" : 7, "6" : 8, "5" : 9, "4" : 10, "3" : 11, "2" : 12, "J" : 13}

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

def is_five_kind(game):
    return all(c == game[0] for c in game)

def is_four_kind(game):
    for c in game:
        if game.count(c) == 4:
            return True
    return False

def is_full_house(game):
    three_c = False
    two_c = False
    for c in game:
        if game.count(c) == 2:
            two_c = True
            if three_c:
                return True
        if game.count(c) == 3:
            three_c = True
            if two_c:
                return True
    return False

def is_three_kind(game):
    for c in game:
        if game.count(c) == 3:
            return True
    return False

def is_two_pair(game):
    first_c = ""
    for c in game:
        if first_c and first_c != c and game.count(c) == 2:
            return True
        if game.count(c) == 2:
            first_c = c
    return False

def is_one_pair(game):
    for c in game:
        if game.count(c) == 2:
            return True
    return False

def compare_games(game1, game2):
    for i in range(len(game1[0])):
        if STRENGHT[game1[0][i]] < STRENGHT[game2[0][i]]:
            return -1
        elif STRENGHT[game1[0][i]] > STRENGHT[game2[0][i]]:
            return 1
    return 0

def compare_games_2(game1, game2):
    for i in range(len(game1[0])):
        if STRENGHT_2[game1[2][i]] < STRENGHT_2[game2[2][i]]:
            return -1
        elif STRENGHT_2[game1[2][i]] > STRENGHT_2[game2[2][i]]:
            return 1
    return 0

def solve_part1(games, games_count):
    five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card = [], [], [], [], [], [], []
    for game in games:
        if is_five_kind(game[0]):
            five_kind.append(game)
        elif is_four_kind(game[0]):
            four_kind.append(game)
        elif is_full_house(game[0]):
            full_house.append(game)
        elif is_three_kind(game[0]):
            three_kind.append(game)
        elif is_two_pair(game[0]):
            two_pair.append(game)
        elif is_one_pair(game[0]):
            one_pair.append(game)
        else:
            high_card.append(game)

    five_kind = sorted(five_kind, key=cmp_to_key(compare_games))
    four_kind = sorted(four_kind, key=cmp_to_key(compare_games))
    full_house = sorted(full_house, key=cmp_to_key(compare_games))
    three_kind = sorted(three_kind, key=cmp_to_key(compare_games))
    two_pair = sorted(two_pair, key=cmp_to_key(compare_games))
    one_pair = sorted(one_pair, key=cmp_to_key(compare_games))
    high_card = sorted(high_card, key=cmp_to_key(compare_games))

    all_games = five_kind + four_kind + full_house + three_kind + two_pair + one_pair + high_card

    sum = 0
    for games in all_games:
        sum += int(games[1])*games_count
        games_count -= 1

    return sum

def best_char(game):
    frec = {}
    
    for c in game:
        if c != "J":
            if c in frec:
                frec[c] += 1
            else:
                frec[c] = 1

    if frec:
        b_char = max(frec, key=frec.get)
        return b_char
    else:
        return "J"

def solve_part2(games, games_count):
    for game in games:
        b_char = best_char(game[0])
        game[0] = game[0].replace("J", b_char)

    five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card = [], [], [], [], [], [], []
    for game in games:
        if is_five_kind(game[0]):
            five_kind.append(game)
        elif is_four_kind(game[0]):
            four_kind.append(game)
        elif is_full_house(game[0]):
            full_house.append(game)
        elif is_three_kind(game[0]):
            three_kind.append(game)
        elif is_two_pair(game[0]):
            two_pair.append(game)
        elif is_one_pair(game[0]):
            one_pair.append(game)
        else:
            high_card.append(game)

    five_kind = sorted(five_kind, key=cmp_to_key(compare_games_2))
    four_kind = sorted(four_kind, key=cmp_to_key(compare_games_2))
    full_house = sorted(full_house, key=cmp_to_key(compare_games_2))
    three_kind = sorted(three_kind, key=cmp_to_key(compare_games_2))
    two_pair = sorted(two_pair, key=cmp_to_key(compare_games_2))
    one_pair = sorted(one_pair, key=cmp_to_key(compare_games_2))
    high_card = sorted(high_card, key=cmp_to_key(compare_games_2))

    all_games = five_kind + four_kind + full_house + three_kind + two_pair + one_pair + high_card

    sum = 0
    for games in all_games:
        sum += int(games[1])*games_count
        games_count -= 1

    return sum

def part1(lines):
    """Solve part 1."""
    games = []
    for line, count in lines.items():
        games.append(line.split(" "))

    solution = solve_part1(games, len(lines))
    return solution


def part2(lines):
    """Solve part 2."""
    games = []
    for line, count in lines.items():
        game = line.split(" ")
        games.append([game[0], game[1], game[0]])

    solution = solve_part2(games, len(lines))
    return solution


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