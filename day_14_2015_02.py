reindeer = {}
per_sec_data = {}
per_sec_points = {}


def dist_after_time(name, time):
    reindeer_per_sec = {}
    one_trip_time = reindeer[name][1] + reindeer[name][2]
    dist_travelled = 0
    for i in range(time):
        curr_time = i+1
        if curr_time % one_trip_time <= reindeer[name][1] and curr_time % one_trip_time != 0:
            dist_travelled += reindeer[name][0]
            #print str(curr_time) + " : " + str(dist_travelled)
            reindeer_per_sec[curr_time] = dist_travelled
        else:
            #print str(curr_time) + " : " + str(dist_travelled)
            reindeer_per_sec[curr_time] = dist_travelled
    return [name, reindeer_per_sec]


def calc_points(time):
    for sec_time in range(time):
        for name in range(len(reindeer_data)):
            per_sec_data[reindeer_data[name][0]] = reindeer_data[name][1][sec_time+1]
        print per_sec_data
        max_dist_covered = max(per_sec_data.values())
        for name, dist in per_sec_data.items():
            if dist == max_dist_covered:
                if name in per_sec_points:
                    per_sec_points[name] += 1
                else:
                    per_sec_points[name] = 1
    return per_sec_points


with open("day_14_2015_01.txt", "r") as f:
    for line in f:
        new_line = line.strip().split()
        reindeer[new_line[0]] = [int(new_line[3]), int(new_line[6]), int(new_line[13])]

reindeer_data = [dist_after_time(i, 2503) for i in reindeer]
all_sec_data = calc_points(2503)
print "Max points collected : " + str(max(all_sec_data.values()))
