import itertools
containers = []


def correct_requirement(combination, eggnog):
    if sum(combination) == eggnog:
        print combination
        return "Y"
    else:
        return "N"


def calc_combination(containers, eggnog):
    success = 0
    for group_by in range(len(containers)):
        all_combination = [group_by for group_by in itertools.combinations(containers, group_by+1)]
        result_set = [correct_requirement(combination, eggnog) for combination in all_combination]
        success += result_set.count("Y")
        if success > 0:
            return success

with open("day_17_2015_01.txt","r") as f:
    for line in f:
        containers.append(int(line))
    containers.sort()

print "\nNo of possible combinations : " +\
      str(calc_combination(containers, 150))
