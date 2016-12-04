f = open("day_01_2015_01.txt", "r")
ctr = 0
pos = 0
for i in f.read():
    pos += 1
    if i == '(':
        ctr += 1
    else:
        ctr -= 1
    if ctr == -1:
        print pos
        break
print ctr

f.close()