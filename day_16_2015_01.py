ticker_tape = {"children": 3,"cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}
max_match = ["",0]
with open("day_16_2015_01.txt", "r") as f:
    for line in f:
        new_line = line.strip().split()
        match = 0
        aunt_no = new_line[1].strip(":")
        for i in range(2,len(new_line)-1,2):
            character = new_line[i].strip(":")
            value = int(new_line[i+1].strip(","))
            if character in ticker_tape and value == ticker_tape[character]:
                match += 1
        if match > max_match[1]:
            max_match[0] = aunt_no
            max_match[1] = match

print "\nMaximum Matched Value from MFCSAM is : Aunt Sue " + str(max_match[0])
