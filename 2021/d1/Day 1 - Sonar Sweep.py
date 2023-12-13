# Day 1 - Sonar Sweep

import pathlib
import sys
import pandas as pd
import numpy as np

def parse(puzzle_input):
    """Parse input"""
    df = pd.read_csv('data/d11.csv', header=None, names=['entries'])
    ls = df['entries'].tolist()
    return ls

def part1(data):
    """Solve part 1"""
    x = 0
    for index, elem in enumerate(data):
        try:
            if data[index+1]>elem:
                x += 1
        except IndexError:
            print('out of range')
    return x

def part2(data):
    """Solve part 2"""
    slide_ls = []
    for index, elem in enumerate(data):
        try:
            sums = data[index]+data[index+1]+data[index+2]
            slide_ls.append(sums)
        except IndexError:
            print('out of range')
    return slide_ls

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))