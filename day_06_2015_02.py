grid = {}
with open("day_06_2015_01.txt") as f:
    for line in f:
        line_values = line.split()
        #print line_values
        if 'toggle' in line:
            c1 = line_values[1]
            c2 = line_values[3]
            x1 = int(c1.split(',')[0])
            y1 = int(c1.split(',')[1])
            x2 = int(c2.split(',')[0])
            y2 = int(c2.split(',')[1])
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if (x,y) in grid:
                        grid[(x, y)] += 2
                    else:
                        grid[(x, y)] = 2
        elif 'turn on' in line:
            c1 = line_values[2]
            c2 = line_values[4]
            x1 = int(c1.split(',')[0])
            y1 = int(c1.split(',')[1])
            x2 = int(c2.split(',')[0])
            y2 = int(c2.split(',')[1])
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if (x,y) in grid:
                        grid[(x, y)] += 1
                    else:
                        grid[(x, y)] = 1
        else:
            c1 = line_values[2]
            c2 = line_values[4]
            x1 = int(c1.split(',')[0])
            y1 = int(c1.split(',')[1])
            x2 = int(c2.split(',')[0])
            y2 = int(c2.split(',')[1])
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if (x,y) in grid and grid[(x, y)] != 0:
                        grid[(x, y)] -= 1

print sum(grid.values())