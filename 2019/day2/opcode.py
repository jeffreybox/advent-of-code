# dependencies
import os
import csv
import pickle
import numpy as np

# data
filename = 'data'
infile = open(filename,'rb')
data = pickle.load(infile)
infile.close()

# recalibration protocol
def recalibrate(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return program

# run the code
def opcode(program):
    address = 0
    while program[address] != 99:
        if program[address] == 1:
            program[program[address+3]] = program[program[address+1]]+program[program[address+2]]
            address = address+4
        elif program[address] == 2:
            program[program[address+3]] = program[program[address+1]]*program[program[address+2]]
            address = address+4
    return program[0]

print("-----------------------------------")
print("PART 1: ANSWER TO NOUN=12 & VERB=2")
program = data.copy()
print(opcode(recalibrate(program, 12, 2)))
print("-----------------------------------")
print("PART 2: SOLVE FOR X")
print('What do you want to solve for? Puzzle asks for 19690720')
solution = int(input())

def solver(solution):
    for i in np.arange(1,99,1):
        for j in np.arange(1,99,1):
            iterator = data.copy()
            test = opcode(recalibrate(iterator, i, j))
            if test==solution:
                a = i
                b = j
                print("noun: " + str(a) + " verb: " + str(b) + " solution: "+ str(test))
                break
            else: 
                continue
    return a,b

noun, verb = solver(solution)

def final(noun, verb):
    return 100*noun+verb
print('What is 100*noun+verb')
print(final(noun, verb))