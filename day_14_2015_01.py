reindeer = {}


def dist_after_time(reindeer_data, time):
    print "Checking for Reindeer : " + reindeer_data + str(reindeer[reindeer_data]) + " for " + str(time) + " Seconds"
    one_trip_time = reindeer[reindeer_data][1] + reindeer[reindeer_data][2]
    no_full_trip = time/one_trip_time
    full_trip_time = no_full_trip * one_trip_time
    full_trip_dist = no_full_trip * reindeer[reindeer_data][0] * reindeer[reindeer_data][1]
    add_trip_dist = min((time - full_trip_time),reindeer[reindeer_data][1]) * reindeer[reindeer_data][0]
    return full_trip_dist + add_trip_dist

with open("day_14_2015_01.txt", "r") as f:
    for line in f:
        new_line = line.strip().split()
        reindeer[new_line[0]] = [int(new_line[3]), int(new_line[6]), int(new_line[13])]

dist_covered = [dist_after_time(i,2503) for i in reindeer]

print "Maximum Distance is covered " + str(max(dist_covered))
