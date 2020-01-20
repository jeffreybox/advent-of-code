#DEPENDENCIES
import numpy as np
import pandas as pd

#INPUT
df = pd.read_csv('data.csv', header=None)
data = df[0].tolist()

#CONDITION 1: CREATE LIST FROM INPUT
min_input = data[0]
max_input = data[1]
ls = np.arange(data[0],data[1],1)

#PART I: NUMBER OF POSSIBLE COMBOS THAT MEET THE CRITERIA
combinations = []

def adjacents(strinput, combinations):
    strinput = str(strinput)
    #check if next digit increases or is the same
    values = []
    for i in np.arange(5):
        if int(strinput[i+1]) >= int(strinput[i]):
            val = 1
        else:
            val = 0
        values.append(val)    
    #check if there is a duplicate entry side by side
    for i in np.arange(5):
        if int(strinput[i]) == int(strinput[i+1]):
            dup = True
            break
        else:
            dup = False
    #check if both conditions are met
    if sum(values) == 5 and dup == True:
        combinations.append(int(strinput)) 
    return combinations

for l in ls:
    adjacents(l,combinations)

answer1 = len(combinations)

print("total number of combinations that meet the criteria between "+ str(min_input) + " and " + str(max_input) + " is: " + str(answer1))