def calc_max_ingredient(input_data, current):
    print input_data
    print current
    max_val = -1
    for ingredient in input_data:
        indi_value = []
        for i in range(4):
            sum_attr = input_data[ingredient][i] + current[i]
            if sum_attr < 0:
                sum_attr = 0
            indi_value.append(sum_attr)
        score = indi_value[0]*indi_value[1]*indi_value[2]*indi_value[3]
        if max_val < score:
            max_val = score
            used_ingredient = ingredient
            new_values = indi_value
    spoon[used_ingredient] += 1
    print new_values
    print ""
    return new_values


def calc_total_score(input_data, current):
    for i in range(100):
        new_val = calc_max_ingredient(input_data, current)
        print new_val
        current = new_val

spoon = {}
properties = {}
with open("day_15_2015_01.txt", "r") as f:
    for line in f:
        details = []
        new_line = line.strip().split()
        [details.append(int(new_line[attr+1].strip(","))) for attr in range(1, 10, 2)]
        properties[new_line[0]] = details
        spoon[new_line[0]] = 0
zero_value = [0, 0, 0, 0, 0]
calc_total_score(properties, zero_value)
print spoon