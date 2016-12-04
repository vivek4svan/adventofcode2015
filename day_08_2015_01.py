total = 0
not_in_mem = 0
with open("day_08_2015_01.txt") as f:
    for line in f:
        new_line = line.strip()
        not_in_mem += 2
        print new_line
        total += len(new_line)
        length = len(new_line)
        pos = 0
        while pos < length:
            if new_line[pos] == "\\" and new_line[pos+1] == "x":
                not_in_mem += 3
                pos += 3
            elif new_line[pos] == "\\":
                not_in_mem += 1
                pos += 1
            pos += 1

print total
print not_in_mem

'''
"sjdivfriyaaqa\xd2v\"k\"mpcu\"yyu\"en"
"vcqc"
"zbcwgmbpijcxu\"yins\"sfxn"
"yumngprx"
"bbdj"
'''