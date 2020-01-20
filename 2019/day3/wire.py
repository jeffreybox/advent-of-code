# DEPENDENCIES
import os
import numpy as np

# DATA
wire1 = open('wire1.txt', 'r').readlines()
wire1 = wire1[0].split(",")
#print(wire1)

wire2 = open('wire2.txt', 'r').readlines()
wire2 = wire2[0].split(",")
#print(wire2)

# METHODS
def coordinator(coordinate):
    direction = coordinate[0]
    distance = int(coordinate[1:])
    return direction, distance

def matrix(x,y, d1, d2, coordinates):
    for i in np.arange(d2):
        if d1 == 'L':
            x = x-1
        elif d1 == 'R':
            x = x+1
        elif d1 == 'U':
            y = y+1
        else:
            y = y-1
        coord = (x,y)
        coordinates.append(coord)
    return coordinates, x, y

def wirecutter(wire):
    x = 0
    y = 0
    coordinates = []
    for turn in wire:
        d1, d2 = coordinator(turn)
        coordinates, x, y = matrix(x, y, d1, d2, coordinates)
    return coordinates

def intersector(a,b):
    intersection = []
    intersection_set = set(a).intersection(b)
    for intersect in intersection_set:
        intersection.append(intersect)
    return intersection

def manhattan(intersection):
    length_list = []
    cp = (0,0)
    for ray in intersection:
        length_list.append(abs(cp[0]-ray[0])+abs(cp[1]-ray[1]))
    return length_list

# MAIN
def main (wire1, wire2):
    a = wirecutter(wire1)
    b = wirecutter(wire2)
    intersection = intersector(a,b)
    manhattan_distances = manhattan(intersection)
    steplist = []
    for c in intersection:
        i1 = a.index(c)+1 
        i2 = b.index(c)+1
        steplist.append(i1+i2)
    return min(manhattan_distances), min(steplist)

min_manhattan, min_distance = main(wire1, wire2)

print('The minimum Manhattan distance between wire 1 & wire 2 is: ' + str(min_manhattan))
print('The minimum number of steps to an intersection  between wire 1 & wire 2 is: ' + str(min_distance))

