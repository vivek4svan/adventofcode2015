req_gift_paper = 0
req_ribbon_length = 0
with open("day_02_2015.txt") as f:
    for line in f:
        #print line
        dimension = [int(x.strip('\n')) for x in line.split('x')]
        lb = dimension[0]*dimension[1]
        bh = dimension[1]*dimension[2]
        bl = dimension[2]*dimension[0]
        extra = min(lb,bh,bl)
        req_gift_paper += (2*(lb + bh + bl) + extra)
        req_ribbon_length += (2*sorted(dimension)[0] + 2*sorted(dimension)[1]) + (dimension[0]*dimension[1]*dimension[2])
        print sorted(dimension)[0], sorted(dimension)[1]
print req_gift_paper
print req_ribbon_length