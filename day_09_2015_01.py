dist_dict = {}
with open("day_09_2015_01.txt") as f:
    for line in f:
        new_line = line.strip()
        loc_1 = line.split()[0]
        loc_2 = line.split()[2]
        if loc_1 in dist_dict:
            connect_nodes = dist_dict[loc_1]
            connect_nodes.append(loc_2)
        else:
            dist_dict[loc_1] = [loc_2, ]

print dist_dict
