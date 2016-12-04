import math
import itertools
data = {}
happiness = []

with open("day_13_2015_01.txt") as f:
    for line in f:
        new_line = line.strip(".\n").split()
        if new_line[2] == "gain":
            data[new_line[0], new_line[10]] = int(new_line[3])
        else:
            data[new_line[0], new_line[10]] = int(new_line[3])*-1

people = set([data.keys()[i][1] for i in range(len(data))])

no_of_people = len(people)
no_of_ways = math.factorial(no_of_people-1)

for arrange in itertools.permutations(people):
    feel = 0
    for i in range(no_of_people):
        if i == 0:
            left = no_of_people-1
        else:
            left = i-1
        if i == no_of_people-1:
            right = 0
        else:
            right = i+1
        feel += (data[arrange[i],arrange[left]] + data[arrange[i],arrange[right]])
    happiness.append(feel)

print "\nMaximum Happiness is : " + str(max(happiness))
