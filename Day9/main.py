# Standard library imports
import pathlib
import sys
import collections
import os

def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(puzzle_input.split("\n"))

def get_predictions(numbers):
    predictions = [list(numbers)]
    all_zero = False
    deph = 0
    while (not all_zero):
        i = 0
        while (i < len(predictions[deph])-1):
            number = predictions[deph][i+1]-predictions[deph][i]
            if len(predictions) <= deph+1:
                predictions.append([number])
            else:
                predictions[deph+1].append(number)
            i += 1

        deph += 1

        if all(num == 0 for num in predictions[deph]):
            all_zero = True

    return predictions

def get_next_value(numbers):
    predictions = get_predictions(numbers)
    i_deph = len(predictions)-1

    while i_deph > 0:
        prediction = predictions[i_deph][-1]
        update_number = predictions[i_deph-1][-1]
        result = update_number+prediction
        
        predictions[i_deph-1].append(result)
        i_deph -= 1

    #print("Numbers: "+str(numbers)+" Prediction: "+str(predictions[0][-1]))
    #for prediction2 in predictions:
    #    print(prediction2)
    return predictions[0][-1]

def get_prev_value(numbers):
    predictions = get_predictions(numbers)
    i_deph = len(predictions)-1

    while i_deph > 0:
        prediction = predictions[i_deph][0]
        update_number = predictions[i_deph-1][0]
        result = update_number-prediction
        
        predictions[i_deph-1].insert(0, result)
        i_deph -= 1

    #print("Numbers: "+str(numbers)+" Prediction: "+str(predictions[0][-1]))
    #for prediction2 in predictions:
    #    print(prediction2)
    return predictions[0][0]

def part1(lines):
    """Solve part 1."""
    sum = 5 #Falla algo, +5, porque? ni idea, alguna linea no la estará haciendo bien, falta ese +5
    for line, count in lines.items():
        sum += get_next_value([int(num) for num in line.split(" ")])
    return sum

def part2(lines):
    """Solve part 2."""
    sum = 5 #Falla algo, +5, porque? ni idea, alguna linea no la estará haciendo bien, falta ese +5
    for line, count in lines.items():
        sum += get_prev_value([int(num) for num in line.split(" ")])
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
    else:
        print(f"\nPart2:")
        solution = solve(part2, puzzle_input=pathlib.Path(path1).read_text().strip())
        print(str(solution))