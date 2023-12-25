# Standard library imports
import pathlib
import sys
import collections
import os

A_MAPS = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", 
          "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

locations_minimum = []

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

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
    
    def get_destination_start(self):
        return self.destination_start
    
    def get_source_start(self):
        return self.source_start
    
    def get_lenght(self):
        return self.lenght
        
    def get_destination_mod(self, value):
        next_value = value-self.source_start
        return self.destination_start+next_value
        
    def __str__(self):
        return f"Destination_Start: {str(self.destination_start)} Source_Start: {str(self.source_start)} Lenght: {str(self.lenght)}"

def get_linemap_with_source(source, map) -> LineMap:
    for line in map:
        if line.is_source(source):
            return line
    return None

def get_location_maps(next_location, maps):
    for nmap in A_MAPS:
        next_location = get_location(next_location, maps[nmap])

    return next_location

def get_location(location, map):
    i = 0
    next_location = location
    while i < len(map) and not map[i].is_source(location):
        i += 1

    if i < len(map):
        next_location = map[i].get_destination_mod(next_location)

    return next_location

def get_next_possible_line(source, lenght, map) -> LineMap:
    line_map = None
    min_value = float("inf")
    for line in map:
        max_range = line.get_source_start() + line.get_lenght()
        if (source + lenght) > line.get_source_start() and (source + lenght) < max_range:
            next_value = line.get_source_start() 
            if next_value < min_value:
                min_value = next_value
                line_map = line
    return line_map

def get_recursion_location_maps(source, lenght, maps, i_map):
    next_source = source
    i_map_aux = i_map
    for nmap in A_MAPS[i_map:len(A_MAPS)]:
        map = maps[nmap]
        i = 0
        while i < len(map) and not map[i].is_source(next_source):
            i += 1

        if i < len(map):
            line_map = map[i]
            source = next_source
            next_source = line_map.get_destination_mod(source)
            aux_source = source-line_map.get_source_start()
            max_lenght = line_map.get_lenght()-aux_source
            if lenght > max_lenght and max_lenght > 0:
                #print(str(lenght)+" "+str(max_lenght))
                new_lenght = lenght-max_lenght
                get_recursion_location_maps(source+max_lenght, new_lenght, maps, i_map_aux)
        else:
            line_map = get_next_possible_line(next_source, lenght, map)
            if line_map:
                source = line_map.get_source_start()
                new_lenght = lenght+(next_source-source)
                #print("source: "+str(source)+ " next_source: "+str(next_source)+ " lenght: "+str(lenght)+ " new_lenght: "+str(new_lenght))
                get_recursion_location_maps(source, new_lenght, maps, i_map_aux)

        i_map_aux += 1

    locations_minimum.append(next_source)

def get_min_location_seeds(seed, lenght_seeds, maps):
    get_recursion_location_maps(seed, lenght_seeds, maps, 0)
    return min(locations_minimum)
    
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
        location = get_location_maps(int(seed), maps)
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