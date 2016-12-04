nice_str = 0
with open("day_05_2015_01.txt") as f:
    for line in f:
        print line
        print "Check1"
        if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
            continue
        print "Check2"
        ctr = 0
        for i in range(len(line)):
            if line[i] in 'aeiouAEIOU':
                ctr += 1
        if ctr < 3:
            continue
        print "Check3"
        for i in range(len(line) - 1):
            if ord(line[i+1]) - ord(line[i]) == 0:
                print "Passed"
                nice_str += 1
                print "Output : " + str(nice_str)
                break
print nice_str