# Standard library imports
import pathlib
import sys
import collections
import os
from math import floor

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

def get_number_of_ways_to_beat_record(race):
    time = race[0]
    distance = race[1]
    ways = 0
    for i in range(1, time):
        time_available = time - i
        traveled = time_available*i
        #print("speed: "+str(i)+ " tiempo: "+str(time_available)+ " recorrido "+str(traveled))
        if (traveled >= distance):
            ways += 1
    return ways

def part1(lines):
    """Solve part 1."""
    races = []
    for line, count in lines.items():
        if "Time:" in line:
            line = line.lstrip("Time:")
            times = line.split(" ")
            for time in times:
                if time:
                    races.append([int(time)])
        if "Distance:" in line:
            line = line.lstrip("Distance:")
            distances = line.split(" ")
            i = 0
            for distance in distances:
                if distance:
                    races[i].append(int(distance))
                    i += 1

    solution = 1 #mult          
    for race in races:
        ways = get_number_of_ways_to_beat_record(race)
        solution = solution * ways

    return solution


def part2(lines):
    """Solve part 2."""
    races = []
    for line, count in lines.items():
        if "Time:" in line:
            line = line.lstrip("Time:")
            times = line.split(" ")
            for time in times:
                if time:
                    if len(races) > 0:
                        races[0] = races[0]+time
                    else:
                        races.append(time)
        if "Distance:" in line:
            line = line.lstrip("Distance:")
            distances = line.split(" ")
            for distance in distances:
                if distance:
                    if len(races) > 1:
                        races[1] = races[1]+distance
                    else:
                        races.append(distance)

    race = [int(value) for value in races]

    solution = get_number_of_ways_to_beat_record(race)

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