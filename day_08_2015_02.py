extra_char = 0
with open("day_08_2015_01.txt") as f:
    for line in f:
        new_line = line.strip()
        extra_char += 4  # 2 for quotes and 2 for escaping existing quotes
        length = len(new_line)
        pos = 0
        while pos < length:
            if new_line[pos] == "\\" and new_line[pos+1] == "\\":
                extra_char += 2
                pos += 2
            if new_line[pos] == "\\" and new_line[pos+1] == "\"":
                extra_char += 2
                pos += 2
            elif new_line[pos] == "\\":
                extra_char += 1
                pos += 1
            else:
                pos += 1
print extra_char

print "\"trajs\\x5brom\\xf1yoijaumkem\\\"\\\"tahlzs\""


'''
"sjdivfriyaaqa\xd2v\"k\"mpcu\"yyu\"en"
"vcqc"
"zbcwgmbpijcxu\"yins\"sfxn"
"yumngprx"
"bbdj"
'''