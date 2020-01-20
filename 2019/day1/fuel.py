# dependencies
import pandas as pd

# read in csv as dataframe
df = pd.read_csv('data.csv', header=None, names=['mass'])

# convert to list
masses = df['mass'].to_list()

# round down any number
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

# calculate the fuel for any given mass
def calculator(num):
    fuel = truncate(num/3)-2
    return fuel

# PART I
total = 0
for mass in masses:
    total = total + calculator(mass)
print("part 1 total: " + str(int(total)))

# calculate the cumulative fuel for any given module
def modules(current):
    total = 0
    while calculator(current) > 0:
        value = calculator(current)
        total = total + value
        current = value
    return total

# PART II
grand_total = 0

for mass in masses:
    grand_total = grand_total + modules(mass)

print("part 2 grand total: " + str(int(grand_total)))
