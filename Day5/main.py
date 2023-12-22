# Standard library imports
import pathlib
import sys
import collections
import os

A_MAPS = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", 
          "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

class LineMap:
    def __init__(self, destination_start, source_start, lenght):
        self.destination_start = int(destination_start)
        self.source_start = int(source_start)
        self.lenght = int(lenght)

    def is_source(self, value):
        #print(str(self.source_start)+" "+str(value)+" "+str(self.source_start+self.lenght))
        if value >= self.source_start and value <= self.source_start+self.lenght:
            return True
        return False
    
    def get_lenght(self):
        return int(self.lenght)
        
    def get_destination_mod(self, value):
        next_value = value-self.source_start
        return self.destination_start+next_value
        
    def __str__(self):
        return f"Destination_Start: {str(self.destination_start)} Source_Start: {str(self.source_start)} Lenght: {str(self.lenght)}"

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

def get_location_seeds(seed, last_seed, maps, min_location):
    line_map = get_seed(seed, maps)
    if line_map.get_destination_mod(seed) < min_location:
        min_location = line_map.get_destination_mod(seed)

    if line_map.get_lenght()+line_map.get_source_start() < last_seed:
        return get_location_seeds(line_map.get_lenght()+line_map.get_source_start(), last_seed, maps, min_location)
    else:
        return min_location

def get_min_location_seeds(seed, last_seed, maps):
    , float("inf")

    map = maps["seed-to-soil"]

    line_map = get_seed(seed, maps)
    if line_map.get_destination_mod(seed) < min_location:
        min_location = line_map.get_destination_mod(seed)

    if line_map.get_lenght()+line_map.get_source_start() < last_seed:
        return get_location_seeds(line_map.get_lenght()+line_map.get_source_start(), last_seed, maps, min_location)
    else:
        return min_location

def get_location(next_location, maps):
    for nmap in A_MAPS:
        map = maps[nmap]
        i = 0
        while i < len(map) and not map[i].is_source(next_location):
            i += 1

        if i < len(map):
            next_location = map[i].get_destination_mod(next_location)

    return next_location

def part1(lines):
    """Solve part 1."""
    seeds = []
    map_name = ""
    maps = {}

    #Creation of Maps
    for line, count in lines.items():
        if "seeds" in line:
            #seeds: 2041142901 113138307 302673608 ....
            seeds = line.lstrip("seeds: ").split(" ")

        #soil-to-fertilizer map: ...
        if "map" in line:
            map_name = line.rstrip(" map:")
            maps[map_name] = []

        if map_name:
            if line[0].isnumeric():
                destination, source, lenght = line.split(" ")
                maps[map_name].append(LineMap(destination, source, lenght))

    min_location = float("inf")
    for seed in seeds:
        location = get_location(int(seed), maps)
        #print("seed: "+ seed+ " location: "+str(location))
        if location < min_location:
            min_location = location

    return min_location


def part2(lines):
    """Solve part 2."""
    seeds = []
    map_name = ""
    maps = {}

    #Creation of Maps
    for line, count in lines.items():
        if "seeds" in line:
            #seeds: 2041142901 113138307 302673608 ....
            seeds = line.lstrip("seeds: ").split(" ")

        #soil-to-fertilizer map: ...
        if "map" in line:
            map_name = line.rstrip(" map:")
            maps[map_name] = []

        if map_name:
            if line[0].isnumeric():
                destination, source, lenght = line.split(" ")
                maps[map_name].append(LineMap(destination, source, lenght))

    min_location = float("inf")
    for i in range(len(seeds)):
        if i%2==0:
            seed = int(seeds[i])
            lenght_seeds =  int(seeds[i+1])
            location = get_min_location_seeds(seed, lenght_seeds, maps)
            if location < min_location:
                min_location = location
        i += 1

    return min_location


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