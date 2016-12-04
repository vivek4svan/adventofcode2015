nice_str = 0
with open("day_05_2015_01.txt","r") as f:
    for line in f:
        new_line = line.strip('\n')
        flag = 0
        for i in range(len(new_line)-1):
            pair = new_line[i:i+2]
            if new_line.count(pair) > 1:
                flag = 1
                break
        if flag == 1:
            flag = 0
            for i in range(len(new_line)-2):
                if new_line[i] == new_line[i+2]:
                    flag = 1
                    nice_str += 1
                    break

print nice_str




'''
It contains a pair of any two letters that appears at
least twice in the string without overlapping,
like xyxy (xy) or aabcdefgaa (aa),but not like aaa
(aa, but it overlaps).
It contains at least one letter which repeats with
exactly one letter between them, like xyx, abcdefeghi (efe),
or even aaa.
'''
